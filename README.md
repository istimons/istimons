# School Management Platform

A comprehensive SaaS platform for elite private schools, built with Django (backend) and Next.js (frontend).

## Features

- Multi-tenant architecture for multiple schools
- Role-based access control with 18+ user roles
- Admissions, student management, academics, finance, communication, and more
- Mobile-friendly responsive design
- Secure JWT authentication
- RESTful APIs with DRF

## Setup Instructions

### Backend

1. cd backend
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver

### Frontend

1. cd frontend
2. npm install
3. npm run dev

## Environment Variables

Create .env in backend:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3

## API Endpoints

- POST /api/auth/register/ - Register user
- POST /api/auth/login/ - Login
- GET /api/auth/profile/ - User profile
- GET/PUT /api/schools/settings/ - School settings

## Production

Use Docker, PostgreSQL, Redis for production.

Run gunicorn for backend, next build for frontend.