# 🛒 E-commerce Enterprise API

![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.12-yellow.svg)
![Django](https://img.shields.io/badge/django-5.0-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

A production-ready, scalable RESTful API designed for modern e-commerce platforms. Built with **Django REST Framework**, this API features robust security, JWT authentication, Docker containerization, and comprehensive API documentation via Swagger/OpenAPI.

---

## 🚀 Features

### Core Functionality

- **Product Management:** Full CRUD operations with rich data support.
- **Category Organization:** Hierarchical categorization of inventory.
- **User Management:** Secure registration and profile management.
- **Search & Filtering:** Advanced filtering by category, price, and stock status.
- **Pagination:** Optimized data delivery for large datasets.

### Enterprise Features

- **JWT Authentication:** Stateless, secure authentication for mobile & SPA clients.
- **Role-Based Access Control (RBAC):** Granular permissions (Admins vs Customers).
- **Throttling & Rate Limiting:** Protection against DDoS and API abuse.
- **Dockerized:** Fully containerized for consistent deployment across environments.
- **Swagger UI:** Interactive, auto-generated API documentation.

---

## 🛠 Tech Stack

- **Framework:** Django 5 & Django REST Framework
- **Database:** PostgreSQL (Production) / SQLite (Dev)
- **Authentication:** SimpleJWT (JSON Web Tokens)
- **Documentation:** drf-yasg (Swagger/Redoc)
- **Containerization:** Docker & Docker Compose
- **Utilities:** Python-Decouple (Env vars), Gunicorn (WSGI)

---

## 📖 API Documentation

The API comes with interactive documentation. Once the server is running, access it at:

- **Swagger UI:** `http://localhost:8000/swagger/`
- **ReDoc:** `http://localhost:8000/redoc/`

---

## 🔧 Installation & Setup

### Option A: Docker (Recommended)

Run the entire application with a single command.

```bash
# 1. Clone the repository
git clone https://github.com/Musakalamz/E-commerce_API.git
cd E-commerce_API

# 2. Build and run containers
docker-compose up --build
```

The API will be available at `http://localhost:8000/api/`.

### Option B: Local Development (Manual)

1. **Clone and Setup Environment**

   ```bash
   git clone https://github.com/Musakalamz/E-commerce_API.git
   cd E-commerce_API
   python -m venv venv
   # Windows:
   .\venv\Scripts\Activate
   # Mac/Linux:
   source venv/bin/activate
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   Create a `.env` file in the root directory:

   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

4. **Run Migrations & Server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## 🧪 Testing

The project includes a comprehensive test suite covering models, serializers, and API endpoints.

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test api
```

---

## 🔒 Security Measures

- **Environment Variables:** Secrets management using `.env` files.
- **Sanitized Inputs:** Django ORM prevents SQL injection.
- **CORS Configuration:** Controlled cross-origin resource sharing.
- **Rate Limiting:** Prevents brute-force attacks on sensitive endpoints.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
