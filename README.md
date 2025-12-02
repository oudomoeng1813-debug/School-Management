# school_management (Generated Django project)

## Overview
This is a minimal Django 5.x project skeleton with an app `app_school` containing models:
- Student
- Subject
- Teacher

The project includes simple AdminLTE-like layout (bootstrap-based) and CRUD pages for all models.

## Setup instructions

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

2. Install Django 5.x:
   ```bash
   pip install "django>=5.0,<6.0"
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. (Optional) Load sample data:
   ```bash
   python manage.py loaddata sample_data.json
   ```

5. Create superuser (for admin site):
   ```bash
   python manage.py createsuperuser
   ```

6. Run server:
   ```bash
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ to view the app.
# School-Management
