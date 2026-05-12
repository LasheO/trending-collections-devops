# Software Development Life Cycle (SDLC) Documentation

> This document outlines the Software Development Life Cycle approach used in the Trending Collections DevOps project, demonstrating structured development methodology aligned with industry best practices.

**Author:** Lashe Onamusi  
**Module:** Software Engineering & DevOps  
**Date:** December 2026

---

## Table of Contents

1. [Overview](#overview)
2. [SDLC Model](#sdlc-model)
3. [Phase 1: Planning](#phase-1-planning)
4. [Phase 2: Design](#phase-2-design)
5. [Phase 3: Development](#phase-3-development)
6. [Phase 4: Testing](#phase-4-testing)
7. [Phase 5: Deployment](#phase-5-deployment)
8. [Phase 6: Maintenance](#phase-6-maintenance)
9. [DevOps Integration](#devops-integration)

---

## Overview

The Trending Collections DevOps project follows an **Agile-DevOps hybrid SDLC** model, combining:
- **Agile principles** for iterative development
- **DevOps practices** for continuous integration and deployment
- **Security-first approach** integrating security testing throughout the lifecycle

### SDLC Benefits

- ✅ Structured development process
- ✅ Early bug detection through continuous testing
- ✅ Automated quality assurance
- ✅ Rapid deployment cycles
- ✅ Continuous feedback and improvement

---

## SDLC Model

### Chosen Approach: **Agile with DevOps**

```
┌──────────────────────────────────────────────────────────┐
│                    CONTINUOUS CYCLE                       │
│                                                           │
│  ┌─────────┐    ┌────────┐    ┌─────────┐    ┌─────────┐│
│  │Planning │ -> │ Design │ -> │  Develop│ -> │  Test   ││
│  └─────────┘    └────────┘    └─────────┘    └─────────┘│
│       ↑                                            │      │
│       │         ┌──────────┐    ┌─────────┐      │      │
│       └─────────│Maintain  │ <- │ Deploy  │ <────┘      │
│                 └──────────┘    └─────────┘              │
│                                                           │
│              DevOps Automation Layer                      │
│  ┌─────────────────────────────────────────────────────┐ │
│  │  CI/CD | Containerization | Monitoring | Testing    │ │
│  └─────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

**Why This Model?**
- **Flexibility**: Adapt to changing requirements quickly
- **Speed**: Rapid iteration and deployment
- **Quality**: Automated testing catches issues early
- **Collaboration**: DevOps bridges development and operations

---

## Phase 1: Planning

### Objectives

Define project requirements, scope, and technical specifications for a secure web application demonstrating DevOps practices.

### Activities

#### 1.1 Requirements Gathering

**Functional Requirements:**
- User authentication and authorization system
- CRUD operations for trending collections
- Role-based access control (Admin vs Regular users)
- Data persistence with relational database
- RESTful API architecture
- Responsive web interface

**Non-Functional Requirements:**
- **Security**: OWASP Top 10 vulnerability protection
- **Performance**: Response time < 2 seconds
- **Scalability**: Containerized for horizontal scaling
- **Reliability**: 99% uptime with health checks
- **Maintainability**: Clean code, documentation, linting

**DevOps Requirements:**
- Automated CI/CD pipeline
- Containerization with Docker
- Code quality automation
- Security testing automation
- Cloud deployment capability

#### 1.2 Technology Selection

**Backend:**
- **Language**: Python 3.11 (mature, extensive libraries)
- **Framework**: Flask (lightweight, flexible)
- **Database**: SQLite (simple, suitable for demo)
- **ORM**: SQLAlchemy (SQL injection protection)
- **Authentication**: JWT (stateless, scalable)

**Frontend:**
- **Framework**: React 18 (component-based, popular)
- **UI Library**: Material-UI (professional components)
- **HTTP Client**: Axios (promise-based, interceptors)

**DevOps Tools:**
- **CI/CD**: GitHub Actions (free, integrated)
- **Containers**: Docker (industry standard)
- **Deployment**: Render (free tier, easy setup)
- **Version Control**: Git/GitHub

#### 1.3 Project Scope

**In Scope:**
- Full-stack web application
- Automated testing (unit, integration, security)
- CI/CD pipeline implementation
- Docker containerization
- Security testing for 3+ OWASP vulnerabilities
- Comprehensive documentation

**Out of Scope:**
- Advanced analytics/reporting
- Third-party integrations
- Mobile applications
- Multiple database support

#### 1.4 Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Security vulnerabilities | High | Automated security testing, OWASP guidelines |
| Deployment failures | Medium | Automated testing before deployment, rollback capability |
| Integration issues | Medium | Docker ensures consistent environments |
| Code quality issues | Low | Automated linting, code reviews |

---

## Phase 2: Design

### Objectives

Create architectural designs, database schemas, and API specifications that support security, scalability, and maintainability.

### Activities

#### 2.1 System Architecture Design

**Architecture Pattern**: Three-Tier Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Presentation Tier (Frontend)                           │
│  - React Components                                      │
│  - Material-UI                                           │
│  - Client-side Routing                                   │
└──────────────────┬──────────────────────────────────────┘
                   │ REST API (HTTPS)
                   │
┌──────────────────▼──────────────────────────────────────┐
│  Application Tier (Backend)                             │
│  - Flask API                                             │
│  - JWT Authentication                                    │
│  - Business Logic                                        │
│  - Input Validation                                      │
└──────────────────┬──────────────────────────────────────┘
                   │ SQLAlchemy ORM
                   │
┌──────────────────▼──────────────────────────────────────┐
│  Data Tier (Database)                                    │
│  - SQLite                                                │
│  - User Table                                            │
│  - TrendingCollection Table                              │
└──────────────────────────────────────────────────────────┘
```

**Design Principles:**
- **Separation of Concerns**: Clear boundaries between layers
- **Security by Design**: Authentication at every layer
- **Scalability**: Stateless API, containerized deployment
- **Maintainability**: Modular code, comprehensive documentation

#### 2.2 Database Design

**User Table Schema:**
```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**TrendingCollection Table Schema:**
```sql
CREATE TABLE trending_collection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_query TEXT NOT NULL,
    trend_topic VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    reformulated_queries TEXT NOT NULL,
    category VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Design Decisions:**
- **Password Hashing**: Werkzeug security for password storage
- **Timestamps**: Track creation and modification times
- **Normalization**: 3NF to reduce data redundancy
- **Indexes**: Primary keys for fast lookups

#### 2.3 API Design

**RESTful API Endpoints:**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/register` | Register new user | No |
| POST | `/api/login` | Authenticate user | No |
| GET | `/api/trends` | List all trends | Yes |
| GET | `/api/trends/:id` | Get specific trend | Yes |
| POST | `/api/trends` | Create new trend | Yes |
| PUT | `/api/trends/:id` | Update trend | Yes |
| DELETE | `/api/trends/:id` | Delete trend | Yes (Admin) |
| GET | `/api/health` | Health check | No |

**API Design Principles:**
- **RESTful**: Standard HTTP methods and status codes
- **Stateless**: JWT tokens for authentication
- **Versioned**: `/api/v1/` for future compatibility
- **Documented**: Clear error messages and responses

#### 2.4 Security Design

**Security Measures:**

1. **Authentication Layer**
   - JWT token-based authentication
   - Password hashing with Werkzeug
   - Token validation on protected routes

2. **Authorization Layer**
   - Role-based access control (RBAC)
   - Admin-only endpoints (delete operations)
   - User identity verification

3. **Input Validation**
   - Email format validation (regex)
   - Required field validation
   - Data type validation

4. **Data Protection**
   - Parameterized queries (SQLAlchemy ORM)
   - Environment variables for secrets
   - CORS configuration

#### 2.5 UI/UX Design

**Design Goals:**
- **Simplicity**: Clean, intuitive interface
- **Responsiveness**: Mobile-friendly design
- **Accessibility**: Proper ARIA labels and semantic HTML
- **Consistency**: Material-UI for consistent components

**Key Screens:**
1. Login/Register Page
2. Dashboard (Trends Grid)
3. Create/Edit Trend Form
4. Admin Controls

---

## Phase 3: Development

### Objectives

Implement the designed system with clean, maintainable code following best practices and DevOps principles.

### Activities

#### 3.1 Development Environment Setup

**Backend Setup:**
```bash
# Virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask sqlalchemy flask-jwt-extended pytest

# Initialize database
python init_db.py
```

**Frontend Setup:**
```bash
# Create React app
npx create-react-app frontend

# Install dependencies
npm install @mui/material axios react-router-dom
```

**DevOps Setup:**
```bash
# Docker configuration
# - Create Dockerfiles
# - Configure docker-compose.yml

# CI/CD configuration
# - GitHub Actions workflows
# - Linting configurations
```

#### 3.2 Backend Development

**Development Approach:**
1. **Models First**: Define database models with SQLAlchemy
2. **API Endpoints**: Implement RESTful routes with Flask
3. **Authentication**: Add JWT token generation and validation
4. **Validation**: Implement input validation and error handling
5. **Testing**: Write unit tests for each component

**Code Organization:**
```
backend/
├── app.py           # Flask application and routes
├── models.py        # Database models
├── init_db.py       # Database initialization
├── create_admin.py  # Admin user creation
└── tests/           # Test suites
```

**Key Implementation Details:**
- **SQLAlchemy ORM**: Prevents SQL injection through parameterized queries
- **Password Hashing**: Werkzeug security for secure password storage
- **JWT Tokens**: Stateless authentication mechanism
- **CORS**: Flask-CORS for frontend communication

#### 3.3 Frontend Development

**Development Approach:**
1. **Component Structure**: Create reusable React components
2. **State Management**: Use React hooks (useState, useEffect)
3. **API Integration**: Axios for HTTP requests
4. **Authentication Flow**: Token storage and API interceptors
5. **UI Components**: Material-UI for consistent design

**Code Organization:**
```
frontend/src/
├── components/
│   ├── Login.js       # Login/Register component
│   └── Dashboard.js   # Main dashboard component
├── App.js             # Main application component
└── index.js           # Entry point
```

**Key Implementation Details:**
- **Token Management**: Store JWT in localStorage
- **API Interceptors**: Automatically attach auth headers
- **Error Handling**: User-friendly error messages
- **Responsive Design**: Material-UI Grid system

#### 3.4 DevOps Implementation

**Containerization:**
- Created Dockerfiles for backend and frontend
- Multi-stage build for optimized frontend image
- Docker Compose for local orchestration
- Non-root containers for security

**CI/CD Pipeline:**
- GitHub Actions workflows for automation
- Automated linting (flake8, ESLint)
- Automated testing (pytest, Jest)
- Automated security testing (OWASP)
- Automated deployment to Render

**Code Quality:**
- Flake8 configuration for Python linting
- ESLint configuration for JavaScript linting
- Pre-commit quality checks
- Coverage reporting

#### 3.5 Development Best Practices

**Code Standards:**
- **PEP 8**: Python style guide compliance
- **Naming Conventions**: Descriptive variable/function names
- **Comments**: Inline documentation for complex logic
- **Modularization**: Single Responsibility Principle
- **DRY**: Don't Repeat Yourself

**Version Control:**
- **Git**: Feature branches for new development
- **Commits**: Descriptive commit messages
- **Pull Requests**: Code review process
- **Tags**: Version tagging for releases

---

## Phase 4: Testing

### Objectives

Ensure application quality, security, and reliability through comprehensive automated testing.

### Activities

#### 4.1 Testing Strategy

**Testing Pyramid:**
```
        ┌─────────┐
        │   E2E   │ (Few)
        └─────────┘
      ┌─────────────┐
      │ Integration │ (Some)
      └─────────────┘
    ┌─────────────────┐
    │  Unit Tests     │ (Many)
    └─────────────────┘
  ┌───────────────────────┐
  │ Security Tests        │ (Critical)
  └───────────────────────┘
```

#### 4.2 Unit Testing

**Backend Unit Tests** (`test_api.py`, `test_models.py`):

```python
# Example unit test
def test_login_success(self):
    response = self.client.post('/api/login', 
        json={'email': 'test@example.com', 'password': 'password123'})
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertIn('token', data)
```

**Test Coverage:**
- User registration and login
- JWT token generation and validation
- CRUD operations for trends
- Admin authorization checks
- Input validation
- Error handling

**Frontend Unit Tests** (Jest + React Testing Library):

```javascript
// Example component test
test('renders dashboard elements', () => {
  render(<Dashboard />);
  expect(screen.getByText('Trending Collections')).toBeInTheDocument();
  expect(screen.getByText('Logout')).toBeInTheDocument();
});
```

**Test Coverage:**
- Component rendering
- User interactions
- Authentication flow
- Error state handling

#### 4.3 Integration Testing

**API Integration Tests:**
- End-to-end API workflows
- Database interaction verification
- Authentication flow testing
- Error response validation

**Testing Approach:**
```python
def test_create_and_delete_flow(self):
    # 1. Login
    token = self.get_auth_token(is_admin=True)
    
    # 2. Create trend
    response = self.client.post('/api/trends', 
        json={...}, headers={'Authorization': f'Bearer {token}'})
    trend_id = response.json['id']
    
    # 3. Verify creation
    response = self.client.get(f'/api/trends/{trend_id}', headers=...)
    self.assertEqual(response.status_code, 200)
    
    # 4. Delete
    response = self.client.delete(f'/api/trends/{trend_id}', headers=...)
    self.assertEqual(response.status_code, 200)
```

#### 4.4 Security Testing

**OWASP Security Test Suite** (`test_security.py`):

**15 Security Tests Covering:**

1. **SQL Injection Prevention (5 tests)**
   - Login email field injection attempts
   - Login password field injection attempts
   - Query parameter injection attempts
   - Database integrity verification
   - Error handling validation

2. **Broken Authentication Prevention (5 tests)**
   - Authentication requirement enforcement
   - Invalid token rejection
   - Token expiration handling
   - Password hashing verification
   - Role-based access control

3. **Cross-Site Scripting Prevention (3 tests)**
   - XSS in registration fields
   - XSS in trend data fields
   - Content-Type header validation

4. **Additional Security (2 tests)**
   - Sensitive data exposure prevention
   - Information leakage in error messages

**Example Security Test:**
```python
def test_sql_injection_login_email(self):
    """Test SQL injection prevention in login"""
    malicious_payloads = [
        "' OR '1'='1' --",
        "admin'--",
        "'; DROP TABLE users; --"
    ]
    
    for payload in malicious_payloads:
        response = self.client.post('/api/login', 
            json={'email': payload, 'password': 'anything'})
        # Should reject, not crash or bypass authentication
        self.assertIn(response.status_code, [400, 401])
```

#### 4.5 Automated Testing in CI/CD

**GitHub Actions Integration:**
```yaml
# Automated testing on every push
- name: Run Backend Unit Tests
  run: pytest tests/test_api.py tests/test_models.py -v

- name: Run OWASP Security Tests
  run: pytest tests/test_security.py -v

- name: Run Frontend Tests
  run: npm test -- --coverage --watchAll=false
```

**Benefits:**
- ✅ Tests run automatically on every commit
- ✅ Prevents broken code from being deployed
- ✅ Fast feedback loop for developers
- ✅ Coverage reports for quality metrics

#### 4.6 Test Results

**Expected Outcomes:**
- **Unit Tests**: 100% pass rate on all core functionality
- **Integration Tests**: All API workflows function correctly
- **Security Tests**: All 15 OWASP tests pass
- **Code Coverage**: >80% for backend, >70% for frontend

---

## Phase 5: Deployment

### Objectives

Deploy the application to production environment with automated deployment pipeline and monitoring.

### Activities

#### 5.1 Deployment Strategy

**Continuous Deployment Approach:**
- Automated deployment on main branch commits
- Tests must pass before deployment
- Health checks after deployment
- Rollback capability if health checks fail

#### 5.2 Containerization

**Docker Images:**
1. **Backend Image**: Python 3.11 slim with Gunicorn
2. **Frontend Image**: Multi-stage build (Node → Nginx)

**Deployment Flow:**
```
Local Development → Docker Build → Docker Registry → Production
        ↓                                               ↓
   docker-compose up                          Render Deployment
```

#### 5.3 Render Deployment

**Configuration** (`render.yaml`):
- Web service for backend (Flask + Gunicorn)
- Static site for frontend (built React app)
- Environment variable management
- Automatic deployment from GitHub

**Deployment Steps:**
1. Push code to GitHub main branch
2. GitHub Actions runs CI/CD pipeline
3. Tests pass → Render automatically deploys
4. Health checks verify deployment success

#### 5.4 Environment Configuration

**Production Environment Variables:**
```env
FLASK_ENV=production
JWT_SECRET_KEY=<secure-random-key>
SQLALCHEMY_DATABASE_URI=sqlite:///production.db
```

**Security Considerations:**
- Secrets stored in Render environment variables (not in code)
- Different secrets for production vs development
- JWT secret key rotated periodically

#### 5.5 Monitoring and Health Checks

**Health Check Endpoint** (`/api/health`):
```python
@app.route('/api/health', methods=['GET'])
def health_check():
    # Check database connection
    # Check API responsiveness
    return jsonify({'status': 'ok', 'database': db_ok})
```

**Monitoring:**
- Render dashboard for deployment status
- GitHub Actions for pipeline status
- Health checks for runtime status

---

## Phase 6: Maintenance

### Objectives

Ensure ongoing system reliability, security updates, and continuous improvement.

### Activities

#### 6.1 Continuous Monitoring

- **Pipeline Monitoring**: GitHub Actions dashboard
- **Application Monitoring**: Render logs and metrics
- **Error Tracking**: Application logs for debugging

#### 6.2 Updates and Patches

**Dependency Management:**
- Regular updates to Python packages
- Regular updates to Node packages
- Security vulnerability scanning
- Breaking change compatibility testing

#### 6.3 Documentation Maintenance

- Keep README.md updated with changes
- Update API documentation for new endpoints
- Update deployment guides for configuration changes
- Document known issues and solutions

#### 6.4 Continuous Improvement

**Future Enhancements:**
- Additional OWASP vulnerability coverage
- Performance optimization
- Enhanced monitoring and alerting
- Additional features based on feedback

---

## DevOps Integration

### How DevOps Enhances the SDLC

#### 1. **Planning → DevOps**
- Infrastructure as Code planning
- CI/CD pipeline design
- Containerization strategy

#### 2. **Design → DevOps**
- Microservices architecture consideration
- Scalability design
- Monitoring design

#### 3. **Development → DevOps**
- Version control with Git
- Feature branches and pull requests
- Code review process

#### 4. **Testing → DevOps**
- Automated testing in CI/CD
- Continuous testing on every commit
- Security testing automation

#### 5. **Deployment → DevOps**
- Automated deployment pipeline
- Containerized deployment
- Zero-downtime deployment

#### 6. **Maintenance → DevOps**
- Continuous monitoring
- Automated alerts
- Rapid rollback capability

### DevOps Cultural Impact

**Collaboration:**
- Dev and Ops work together from planning
- Shared responsibility for quality
- Transparent communication through documentation

**Automation:**
- Reduce manual errors
- Faster delivery cycles
- Consistent, repeatable processes

**Continuous Improvement:**
- Feedback loops at every stage
- Metrics-driven decisions
- Iterative enhancements

---

## Conclusion

The Trending Collections DevOps project demonstrates a comprehensive SDLC approach that integrates:

✅ **Structured Planning**: Clear requirements and technology selection  
✅ **Thoughtful Design**: Security-first architecture and API design  
✅ **Quality Development**: Best practices, modular code, documentation  
✅ **Comprehensive Testing**: Unit, integration, and security testing  
✅ **Automated Deployment**: CI/CD pipeline with containerization  
✅ **Continuous Maintenance**: Monitoring, updates, and improvements  

By integrating DevOps practices throughout the SDLC, the project achieves:
- **Faster** delivery cycles through automation
- **Higher quality** through continuous testing
- **Better security** through automated security testing
- **More reliability** through containerization and monitoring

---

**Document Version:** 1.0  
**Last Updated:** December 2026  
**Author:** Lashe Onamusi
