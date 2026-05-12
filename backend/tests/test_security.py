"""
OWASP Top 10 Security Test Suite

This module tests the application's defenses against common web vulnerabilities
as defined by the OWASP Top 10. These tests are critical for demonstrating
security best practices in the DevOps pipeline.

Tests cover:
1. SQL Injection Prevention (A03:2021 - Injection)
2. Broken Authentication Prevention (A07:2021 - Identification and Authentication Failures)
3. Cross-Site Scripting (XSS) Prevention (A03:2021 - Injection)

Author: Lashe Onamusi
Date: December 2026
Purpose: University DevOps Assignment - Security Testing
"""

import unittest
import json
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, db
from models import User, TrendingCollection


class SecurityTestCase(unittest.TestCase):
    """Test suite for OWASP Top 10 vulnerability prevention"""
    
    def setUp(self):
        """Set up test environment before each test"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
            
            # Create test user
            test_user = User(email='security@test.com', is_admin=False)
            test_user.set_password('securepass123')
            
            # Create test trend
            test_trend = TrendingCollection(
                original_query='Test Query',
                trend_topic='Test Topic',
                description='Test Description',
                reformulated_queries='Test Queries',
                category='Test'
            )
            
            db.session.add(test_user)
            db.session.add(test_trend)
            db.session.commit()
    
    def tearDown(self):
        """Clean up after each test"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def get_auth_token(self):
        """Helper method to get valid auth token"""
        response = self.client.post('/api/login', 
            json={'email': 'security@test.com', 'password': 'securepass123'})
        return json.loads(response.data)['token']
    
    # =============================================================================
    # OWASP A03:2021 - SQL INJECTION PREVENTION TESTS
    # =============================================================================
    
    def test_sql_injection_login_email(self):
        """
        Test: SQL Injection in Login Email Field
        
        OWASP Category: A03:2021 - Injection
        
        Attack Scenario: Hacker tries to bypass authentication by injecting
        SQL code into the email field (e.g., ' OR '1'='1' --).
        
        Expected: Application should safely handle the input using parameterized
        queries (SQLAlchemy ORM), preventing SQL injection. Login should fail
        with invalid credentials message.
        """
        malicious_payloads = [
            "' OR '1'='1' --",
            "admin'--",
            "' OR 1=1--",
            "admin' OR '1'='1",
            "'; DROP TABLE users; --"
        ]
        
        for payload in malicious_payloads:
            response = self.client.post('/api/login', 
                json={'email': payload, 'password': 'anything'})
            
            # Should return 400 (invalid email format) or 401 (invalid credentials)
            # NOT 200 (successful login) or 500 (SQL error)
            self.assertIn(response.status_code, [400, 401], 
                f"SQL injection payload '{payload}' was not properly handled")
            
            # Should not crash the application with SQL error
            if response.status_code == 500:
                self.fail(f"SQL injection caused server error: {payload}")
    
    def test_sql_injection_login_password(self):
        """
        Test: SQL Injection in Login Password Field
        
        OWASP Category: A03:2021 - Injection
        
        Attack Scenario: Hacker tries SQL injection through password field.
        
        Expected: Password hashing and parameterized queries prevent injection.
        """
        response = self.client.post('/api/login', 
            json={'email': 'security@test.com', 
                  'password': "' OR '1'='1' --"})
        
        # Should fail authentication, not bypass it
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_sql_injection_search_parameter(self):
        """
        Test: SQL Injection via Query Parameters
        
        OWASP Category: A03:2021 - Injection
        
        Attack Scenario: If search functionality existed, test that query
        parameters cannot inject SQL.
        
        Expected: SQLAlchemy ORM automatically prevents SQL injection in queries.
        """
        token = self.get_auth_token()
        
        # Test with potential SQL injection in URL parameters (if implemented)
        # For now, we test that the API doesn't expose raw SQL
        response = self.client.get('/api/trends', 
            headers={'Authorization': f'Bearer {token}'})
        
        # Should work normally
        self.assertEqual(response.status_code, 200)
        
        # Verify database integrity wasn't compromised
        with self.app.app_context():
            user_count = User.query.count()
            trend_count = TrendingCollection.query.count()
            self.assertEqual(user_count, 1, "Database integrity compromised")
            self.assertEqual(trend_count, 1, "Database integrity compromised")
    
    # =============================================================================
    # OWASP A07:2021 - BROKEN AUTHENTICATION PREVENTION TESTS
    # =============================================================================
    
    def test_authentication_required_for_trends(self):
        """
        Test: Authentication Required to Access Protected Resources
        
        OWASP Category: A07:2021 - Identification and Authentication Failures
        
        Attack Scenario: Hacker tries to access protected endpoints without
        providing authentication token.
        
        Expected: Server should return 401 Unauthorized and deny access.
        """
        # Try to access trends without authentication
        response = self.client.get('/api/trends')
        
        self.assertEqual(response.status_code, 401, 
            "Unauthenticated access should be denied")
    
    def test_invalid_token_rejected(self):
        """
        Test: Invalid/Fake JWT Tokens are Rejected
        
        OWASP Category: A07:2021 - Identification and Authentication Failures
        
        Attack Scenario: Hacker provides a fake or malformed JWT token to
        try to bypass authentication.
        
        Expected: Server validates JWT signature and rejects fake tokens.
        """
        fake_tokens = [
            'Bearer fake.token.here',
            'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.invalid',
            'InvalidFormat',
            ''
        ]
        
        for fake_token in fake_tokens:
            response = self.client.get('/api/trends',
                headers={'Authorization': fake_token})
            
            # Should reject with 401 or 422 (unprocessable)
            self.assertIn(response.status_code, [401, 422],
                f"Fake token '{fake_token}' should be rejected")
    
    def test_expired_token_handling(self):
        """
        Test: Token Expiration Handling
        
        OWASP Category: A07:2021 - Identification and Authentication Failures
        
        Note: Current implementation has tokens that don't expire (for development).
        In production, tokens should expire and be rejected after expiration.
        
        This test documents the expected behavior for production.
        """
        # Get a valid token
        token = self.get_auth_token()
        
        # In current implementation, token should work
        response = self.client.get('/api/trends',
            headers={'Authorization': f'Bearer {token}'})
        
        self.assertEqual(response.status_code, 200)
        
        # NOTE: In production deployment, implement token expiration
        # and this test should verify expired tokens are rejected
    
    def test_password_hashing_prevents_plaintext_storage(self):
        """
        Test: Passwords are Hashed, Not Stored in Plaintext
        
        OWASP Category: A07:2021 - Identification and Authentication Failures
        
        Attack Scenario: If database is compromised, passwords should not be
        readable in plaintext.
        
        Expected: Passwords are hashed using secure algorithm (bcrypt/werkzeug).
        """
        with self.app.app_context():
            user = User.query.filter_by(email='security@test.com').first()
            
            # Password hash should NOT equal the plaintext password
            self.assertNotEqual(user.password_hash, 'securepass123',
                "Password should be hashed, not stored in plaintext")
            
            # Password hash should be significantly different from original
            self.assertGreater(len(user.password_hash), 20,
                "Password hash should be long (hashed)")
            
            # Verify the hashing works correctly
            self.assertTrue(user.check_password('securepass123'),
                "Password verification should work")
            self.assertFalse(user.check_password('wrongpassword'),
                "Wrong password should be rejected")
    
    def test_authorization_admin_only_delete(self):
        """
        Test: Role-Based Access Control (Admin vs Regular User)
        
        OWASP Category: A07:2021 - Identification and Authentication Failures
        
        Attack Scenario: Regular user tries to perform admin-only actions
        (e.g., deleting trends).
        
        Expected: Server checks user role and denies access with 403 Forbidden.
        """
        token = self.get_auth_token()  # Regular user token
        
        # Try to delete a trend as regular user
        response = self.client.delete('/api/trends/1',
            headers={'Authorization': f'Bearer {token}'})
        
        # Should be denied with 403 Forbidden (not 401 Unauthorized)
        self.assertEqual(response.status_code, 403,
            "Regular users should not be able to delete trends")
        
        data = json.loads(response.data)
        self.assertIn('Admin privileges required', data['error'])
    
    # =============================================================================
    # OWASP A03:2021 - CROSS-SITE SCRIPTING (XSS) PREVENTION TESTS
    # =============================================================================
    
    def test_xss_prevention_in_registration(self):
        """
        Test: XSS Prevention in User Registration
        
        OWASP Category: A03:2021 - Injection (XSS)
        
        Attack Scenario: Hacker tries to inject malicious JavaScript code
        in registration fields (email, etc.).
        
        Expected: Application validates input format and rejects invalid emails
        containing script tags or JavaScript.
        """
        xss_payloads = [
            '<script>alert("XSS")</script>@example.com',
            'user@example.com<script>alert(1)</script>',
            '<img src=x onerror=alert(1)>@example.com',
            'javascript:alert(1)@example.com'
        ]
        
        for payload in xss_payloads:
            response = self.client.post('/api/register',
                json={'email': payload, 'password': 'password123'})
            
            # Should reject with 400 (invalid email format)
            self.assertEqual(response.status_code, 400,
                f"XSS payload '{payload}' should be rejected")
            
            data = json.loads(response.data)
            self.assertIn('Invalid email format', data['error'])
    
    def test_xss_prevention_in_trend_creation(self):
        """
        Test: XSS Prevention in Trend Data
        
        OWASP Category: A03:2021 - Injection (XSS)
        
        Attack Scenario: Hacker tries to inject XSS payload in trend fields
        (description, topic, queries, etc.).
        
        Expected: Data is stored safely and returned as plain text (not executed).
        React automatically escapes output, but we verify storage is safe.
        """
        token = self.get_auth_token()
        
        xss_payload = {
            'original_query': '<script>alert("XSS")</script>',
            'trend_topic': '<img src=x onerror=alert(1)>',
            'description': '"><script>document.cookie</script>',
            'reformulated_queries': 'javascript:alert(1)',
            'category': '<svg/onload=alert(1)>'
        }
        
        # Create trend with XSS payloads
        response = self.client.post('/api/trends',
            json=xss_payload,
            headers={'Authorization': f'Bearer {token}'})
        
        # Should accept the data (not our job to sanitize content)
        self.assertEqual(response.status_code, 201)
        
        # Retrieve the data
        trend_id = json.loads(response.data)['id']
        response = self.client.get(f'/api/trends/{trend_id}',
            headers={'Authorization': f'Bearer {token}'})
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Verify data is stored as-is (escaped by React on frontend)
        # The key is that it's returned as JSON string, not HTML
        self.assertEqual(data['original_query'], xss_payload['original_query'])
        
        # Response should be JSON, not HTML that could execute scripts
        self.assertEqual(response.content_type, 'application/json')
    
    def test_content_type_headers_prevent_xss(self):
        """
        Test: Proper Content-Type Headers Prevent XSS
        
        OWASP Category: A03:2021 - Injection (XSS)
        
        Attack Scenario: If response isn't properly marked as JSON, browser
        might interpret it as HTML and execute scripts.
        
        Expected: All API responses have proper Content-Type: application/json
        """
        token = self.get_auth_token()
        
        endpoints_to_test = [
            ('/api/trends', 'GET'),
            ('/api/login', 'POST')
        ]
        
        for endpoint, method in endpoints_to_test:
            if method == 'GET':
                response = self.client.get(endpoint,
                    headers={'Authorization': f'Bearer {token}'})
            elif method == 'POST':
                response = self.client.post(endpoint,
                    json={'email': 'security@test.com', 'password': 'securepass123'})
            
            # Verify Content-Type is application/json
            self.assertIn('application/json', response.content_type,
                f"Endpoint {endpoint} should return JSON content type")
    
    # =============================================================================
    # ADDITIONAL SECURITY TESTS
    # =============================================================================
    
    def test_sensitive_data_not_exposed_in_responses(self):
        """
        Test: Sensitive Data Exposure Prevention
        
        OWASP Category: A02:2021 - Cryptographic Failures
        
        Attack Scenario: API responses might accidentally expose sensitive data
        like password hashes, secret keys, etc.
        
        Expected: Only necessary data is returned in API responses.
        """
        token = self.get_auth_token()
        
        response = self.client.get('/api/trends',
            headers={'Authorization': f'Bearer {token}'})
        
        # Check that response doesn't contain sensitive keywords
        response_text = response.data.decode('utf-8')
        
        sensitive_keywords = ['password_hash', 'secret_key', 'JWT_SECRET']
        for keyword in sensitive_keywords:
            self.assertNotIn(keyword, response_text,
                f"Sensitive data '{keyword}' should not be exposed in API response")
    
    def test_error_messages_dont_leak_information(self):
        """
        Test: Error Messages Don't Leak System Information
        
        OWASP Category: A05:2021 - Security Misconfiguration
        
        Attack Scenario: Detailed error messages might reveal system information
        to attackers (database structure, file paths, etc.).
        
        Expected: Generic error messages that don't reveal internal details.
        """
        # Test with invalid trend ID
        token = self.get_auth_token()
        response = self.client.get('/api/trends/99999',
            headers={'Authorization': f'Bearer {token}'})
        
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        
        # Error message should be generic
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Trend not found')
        
        # Should NOT contain database details, SQL queries, or file paths
        response_text = response.data.decode('utf-8')
        leak_indicators = ['sqlite', 'SELECT', 'FROM', 'WHERE', '/Users/', 'Traceback']
        for indicator in leak_indicators:
            self.assertNotIn(indicator, response_text,
                f"Error message should not contain '{indicator}'")


if __name__ == '__main__':
    # Run the security test suite
    unittest.main(verbosity=2)
