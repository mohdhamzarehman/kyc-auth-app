# KYC Authentication System

A secure KYC-based authentication system built with Django REST Framework, featuring JWT authentication and document verification capabilities.

## Features

- User registration and login with JWT authentication
- KYC document upload and verification
- Secure file storage
- RESTful API endpoints
- CORS support
- Environment variable configuration

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate 
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/auth/register/` - User registration
- `/api/auth/login/` - User login (JWT token)
- `/api/auth/refresh/` - Refresh JWT token
- `/api/kyc/upload/` - Upload KYC documents
- `/api/kyc/status/` - Check KYC verification status

## Security Features

- JWT-based authentication
- Secure file upload handling
- Environment variable configuration
- CORS protection
- Input validation and sanitization 
