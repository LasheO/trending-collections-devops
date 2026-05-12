# Trending Collections DevOps 🚀

> A secure, containerized web application demonstrating DevOps best practices with automated CI/CD pipeline, comprehensive security testing, and cloud deployment.

**Author:** Lashe Onamusi  
**University Module:** Software Engineering & DevOps  
**Date:** December 2026

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [DevOps Pipeline](#devops-pipeline)
- [Security](#security)
- [Testing](#testing)
- [Deployment](#deployment)
- [Documentation](#documentation)

---

## 🎯 Overview

Trending Collections is a full-stack web application that allows users to manage and browse trending search collections. The application demonstrates modern DevOps practices including:

- **Automated CI/CD Pipeline** with GitHub Actions
- **Containerization** with Docker
- **Security Testing** for OWASP Top 10 vulnerabilities
- **Code Quality Automation** with linting and testing
- **Cloud Deployment** on Render
- **Comprehensive Testing** (Unit, Integration, Security)

### Application Features

- 🔐 **User Authentication** - Secure JWT-based authentication
- 👥 **Role-Based Access Control** - Admin and regular user roles
- 📊 **CRUD Operations** - Create, Read, Update, Delete trending collections
- 🔍 **Data Management** - Browse and filter trending topics
- ✅ **Input Validation** - Comprehensive validation and error handling
- 🛡️ **Security** - Protection against SQL injection, XSS, and broken authentication

---

## ✨ Features

### Functional Features
- User registration and login with password hashing
- JWT token-based authentication and authorization
- Admin-only delete functionality (role-based access control)
- Create and update trending collection entries
- View all trending collections with filtering
- Email format validation
- Database persistence with SQLite

### DevOps Features
- **CI/CD Pipeline**: Automated testing, building, and deployment
- **Containerization**: Docker containers for consistent environments
- **Security Testing**: Automated OWASP vulnerability testing
- **Code Quality**: Linting with flake8 and ESLint
- **Test Coverage**: Unit tests, integration tests, and security tests
- **Health Monitoring**: Health check endpoints for monitoring
- **Documentation**: Comprehensive technical documentation

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python 3.11)
- **Database**: SQLAlchemy with SQLite
- **Authentication**: Flask-JWT-Extended
- **API**: RESTful API with CORS support
- **Server**: Gunicorn (production)
- **Testing**: pytest with coverage reporting

### Frontend
- **Framework**: React 18
- **UI Library**: Material-UI (MUI)
- **HTTP Client**: Axios
- **Testing**: Jest with React Testing Library
- **Build Tool**: Create React App
- **Server**: Nginx (production)

### DevOps Tools
- **Version Control**: Git & GitHub
- **CI/CD**: GitHub Actions
- **Containerization**: Docker & Docker Compose
- **Code Quality**: flake8 (Python), ESLint (JavaScript)
- **Deployment**: Render
- **Monitoring**: Health check endpoints

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser)                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTPS
                         │
┌────────────────────────▼────────────────────────────────────┐
│                   Frontend (React + Nginx)                   │
│  - Material-UI Components                                    │
│  - Client-side Routing                                       │
│  - JWT Token Management                                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ REST API
                         │
┌────────────────────────▼────────────────────────────────────┐
│                   Backend (Flask + Gunicorn)                 │
│  - JWT Authentication                                        │
│  - Role-Based Authorization                                  │
│  - Input Validation                                          │
│  - Business Logic                                            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ SQLAlchemy ORM
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    Database (SQLite)                         │
│  - User Table                                                │
│  - TrendingCollection Table                                  │
└──────────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose (optional, for containerized deployment)
- Git

### Local Development (Without Docker)

#### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Create admin user (optional)
python create_admin.py

# Run development server
python app.py
```

Backend will run at `http://localhost:5000`

#### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will run at `http://localhost:3000`

### Docker Deployment (Recommended)

```bash
# From project root directory
docker-compose up --build

# Or run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

---

## 🔄 DevOps Pipeline

The application uses GitHub Actions for automated CI/CD. See [DEVOPS_PIPELINE.md](docs/DEVOPS_PIPELINE.md) for detailed documentation.

### Pipeline Stages

```
┌─────────────────────────────────────────────────────────────┐
│  Stage 1: Code Quality (Linting)                            │
│  - Python: flake8                                            │
│  - JavaScript: ESLint                                        │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  Stage 2: Backend Testing                                    │
│  - Unit Tests (pytest)                                       │
│  - Security Tests (OWASP)                                    │
│  - Coverage Reports                                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  Stage 3: Frontend Testing                                   │
│  - Component Tests (Jest)                                    │
│  - Integration Tests                                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  Stage 4: Build Verification                                 │
│  - Build Production Bundle                                   │
│  - Verify Build Artifacts                                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  Stage 5: Deploy to Render (if main branch)                 │
│  - Automatic Deployment                                      │
│  - Health Check Verification                                 │
└─────────────────────────────────────────────────────────────┘
```

### CI/CD Features

- ✅ Automated testing on every push
- ✅ Code quality checks
- ✅ Security vulnerability scanning
- ✅ Build verification
- ✅ Automatic deployment to production
- ✅ Fast feedback with PR checks

---

## 🔒 Security

The application implements security best practices and defends against OWASP Top 10 vulnerabilities. See [SECURITY.md](docs/SECURITY.md) for comprehensive security documentation.

### Security Features

1. **SQL Injection Prevention**
   - Parameterized queries with SQLAlchemy ORM
   - Input validation and sanitization
   - Automated security testing

2. **Broken Authentication Prevention**
   - JWT token-based authentication
   - Password hashing with Werkzeug
   - Role-based access control (RBAC)
   - Token validation on protected endpoints

3. **Cross-Site Scripting (XSS) Prevention**
   - Email format validation with regex
   - JSON response content-type headers
   - React automatic escaping
   - Input sanitization

4. **Additional Security Measures**
   - Sensitive data not exposed in responses
   - Generic error messages (no information leakage)
   - CORS properly configured
   - Non-root Docker containers
   - Environment variable management

---

## 🧪 Testing

### Test Coverage

The application includes comprehensive testing at multiple levels:

#### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test suites
pytest tests/test_api.py        # API tests
pytest tests/test_models.py     # Model tests
pytest tests/test_security.py   # Security tests
```

**Test Suites:**
- `test_api.py` - API endpoint tests (authentication, CRUD operations)
- `test_models.py` - Database model tests
- `test_security.py` - OWASP security vulnerability tests (15 tests)

#### Frontend Tests

```bash
cd frontend

# Run tests
npm test

# Run with coverage
npm test -- --coverage
```

**Test Coverage:**
- Component rendering tests
- User interaction tests
- Authentication flow tests

### Security Testing

The security test suite includes 15 comprehensive tests covering:
- SQL Injection (5 tests)
- Broken Authentication (5 tests)
- Cross-Site Scripting (3 tests)
- Sensitive Data Exposure (2 tests)

Run security tests:
```bash
cd backend
pytest tests/test_security.py -v
```

---

## 🌐 Deployment

### Render Deployment

The application is configured for automatic deployment to Render via GitHub integration.

**Deployment URL**: [To be added after deployment]

#### Deployment Configuration

The `render.yaml` file configures the deployment:
- Backend service (Flask with Gunicorn)
- Build commands and start commands
- Environment variables
- Health check endpoints

#### Manual Deployment Steps

1. **Create Render Account** at https://render.com
2. **Connect GitHub Repository**
3. **Configure Environment Variables**
4. **Deploy**
   - Render automatically detects the configuration
   - Deployment triggered on push to main branch

#### Environment Variables

Copy `.env.example` to `.env` and configure:

```env
# Backend
FLASK_ENV=production
JWT_SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=sqlite:///app.db

# Frontend
REACT_APP_API_URL=https://your-backend-url.onrender.com
```

---

## 📚 Documentation

Comprehensive documentation is available in the `docs/` directory:

- **[SDLC.md](docs/SDLC.md)** - Software Development Life Cycle documentation
  - Planning Phase
  - Design Phase
  - Development Phase
  - Testing Phase

- **[SECURITY.md](docs/SECURITY.md)** - Security documentation
  - OWASP Top 10 coverage
  - Security testing approach
  - Vulnerability prevention strategies

- **[DEVOPS_PIPELINE.md](docs/DEVOPS_PIPELINE.md)** - DevOps pipeline documentation
  - CI/CD configuration
  - Pipeline stages and tools
  - Evidence of implementation

---

## 📊 Project Structure

```
trending-collections-devops/
├── .github/
│   └── workflows/
│       ├── ci-cd.yml              # Main CI/CD pipeline
│       └── pr-checks.yml          # Pull request checks
├── backend/
│   ├── app.py                     # Flask application
│   ├── models.py                  # Database models
│   ├── requirements.txt           # Python dependencies
│   ├── Dockerfile                 # Backend container
│   ├── .flake8                    # Linting configuration
│   └── tests/
│       ├── test_api.py            # API tests
│       ├── test_models.py         # Model tests
│       └── test_security.py       # Security tests
├── frontend/
│   ├── src/                       # React source code
│   ├── public/                    # Static assets
│   ├── package.json               # Node dependencies
│   ├── Dockerfile                 # Frontend container
│   ├── nginx.conf                 # Nginx configuration
│   └── .eslintrc.json             # Linting configuration
├── docs/
│   ├── SDLC.md                    # SDLC documentation
│   ├── SECURITY.md                # Security documentation
│   └── DEVOPS_PIPELINE.md         # Pipeline documentation
├── docker-compose.yml             # Container orchestration
├── render.yaml                    # Render deployment config
├── .dockerignore                  # Docker exclusions
├── .env.example                   # Environment template
└── README.md                      # This file
```

---

## 🤝 Contributing

This is a university project demonstrating DevOps practices. For educational purposes only.

---

## 📝 License

This project is for educational purposes as part of a university assignment.

---

## 👤 Author

**Lashe Onamusi**
- University Module: Software Engineering & DevOps
- Year: 2026

---

## 🙏 Acknowledgments

- University instructors for DevOps guidance
- OWASP for security best practices
- Open source community for tools and frameworks

---

## 📞 Support

For questions or issues related to this project, please refer to the documentation in the `docs/` directory or contact through the university portal.

---

**Last Updated:** December 2026
