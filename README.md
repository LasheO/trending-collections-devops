# Trending Collections

> A secure full-stack web application for managing and browsing trending search query data. Built with Flask, React, and an automated CI/CD pipeline.

**Author:** Lashe Onamusi
**Module:** Software Engineering & DevOps
**Year:** 2026

---

## 🌐 Live Application

| Service | URL |
|---|---|
| **Frontend** | https://trending-collections-frontend.onrender.com |
| **Backend API** | https://trending-collections-backend.onrender.com |

> ⚠️ The app is hosted on Render's free tier. If it hasn't been accessed recently, it may take up to 30 seconds to wake up on first load.

---

## 🔐 Test Accounts

Two accounts are pre-seeded in the database and ready to use:

| Role | Email | Password | Permissions |
|---|---|---|---|
| **Admin** | admin@example.com | adminpassword123 | Create, edit, and delete all entries |
| **Regular User** | user@example.com | userpassword123 | Create and edit entries only |

---

## 📖 How to Use the App

### Logging In
1. Open the live frontend link above
2. Enter one of the test account credentials
3. Click **Login**

### Browsing Trending Collections
- After logging in, the dashboard displays all trending collection entries
- Each entry shows the original search query, trend topic, category, description, and reformulated queries

### Creating a New Entry
1. Click the **Add Collection** button on the dashboard
2. Fill in the required fields:
   - **Original Query** — the base search term (e.g. "Running Shoes")
   - **Trend Topic** — the specific trend name (e.g. "Neon Trainers")
   - **Category** — the product category
   - **Description** — a brief description of the trend
   - **Reformulated Queries** — alternative search terms for this trend
3. Click **Save**

### Editing an Entry
1. Click the **Edit** (pencil) icon on any entry
2. Update the desired fields
3. Click **Save**

### Deleting an Entry (Admin only)
1. Log in as `admin@example.com`
2. Click the **Delete** (bin) icon on any entry
3. Confirm the deletion

> Regular users do not see the delete button. Attempting to call the delete endpoint without admin credentials returns a `403 Forbidden` response.

---

## 🔗 API Reference

The backend REST API is accessible at `https://trending-collections-backend.onrender.com`.

All endpoints except `/api/register` and `/api/login` require a valid JWT token passed as a Bearer token in the `Authorization` header.

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/api/register` | None | Register a new user |
| `POST` | `/api/login` | None | Log in and receive a JWT token |
| `GET` | `/api/trends` | Required | Retrieve all trending collections |
| `POST` | `/api/trends` | Required | Create a new trending collection |
| `PUT` | `/api/trends/<id>` | Required | Update an existing collection |
| `DELETE` | `/api/trends/<id>` | Admin only | Delete a collection |
| `GET` | `/api/health` | None | Health check endpoint |

---

## 🛡️ Security

The application is tested against three OWASP Top 10 (2025) vulnerability categories:

| OWASP Category | Protection |
|---|---|
| **A05:2025 — Injection** | SQLAlchemy ORM (parameterised queries) + server-side email regex validation |
| **A07:2025 — Authentication Failures** | bcrypt password hashing, JWT token verification, role-based access control |
| **A04:2025 — Cryptographic Failures** | Sensitive fields (password hashes, secret keys) excluded from all API responses |

A dedicated security test suite (`backend/tests/test_security.py`) contains 12 automated tests covering these categories. All tests run automatically in the CI/CD pipeline on every push — deployment is blocked if any test fails.

---

## ⚙️ Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11, Flask, SQLAlchemy, SQLite |
| Authentication | Flask-JWT-Extended, Werkzeug (bcrypt) |
| Frontend | React 18, Material-UI |
| Testing | pytest (backend), Jest (frontend), ESLint (linting) |
| Containers | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Deployment | Render |

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch triggers an automated six-stage pipeline in GitHub Actions:

```
Lint → Backend Tests → Frontend Tests → Security Tests → Build Verification → Deploy
```

Deployment only runs if all five preceding stages pass. The `autoDeploy` flag in `render.yaml` is set to `false`, ensuring deployments can only be triggered through the pipeline.

Pipeline status: [github.com/LasheO/trending-collections-devops/actions](https://github.com/LasheO/trending-collections-devops/actions)

---

## 📁 Repository Structure

```
trending-collections-devops/
├── .github/workflows/       # GitHub Actions CI/CD pipeline
├── backend/
│   ├── app.py               # Flask application & API routes
│   ├── models.py            # Database models (User, TrendingCollection)
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile
│   └── tests/
│       ├── test_api.py      # API endpoint tests
│       ├── test_models.py   # Model unit tests
│       └── test_security.py # OWASP security tests
├── frontend/
│   ├── src/                 # React source code
│   ├── Dockerfile
│   └── nginx.conf
├── docker-compose.yml
├── render.yaml              # Render deployment configuration
└── README.md
```

---

*Software Engineering & DevOps — University Assignment, 2026*
