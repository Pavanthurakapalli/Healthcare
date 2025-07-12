# Healthcare Backend – Django Assignment

This is a backend system for a Healthcare application, built with Django and Django REST Framework (DRF). The system allows user registration, login, and management of doctors and patients, along with secure JWT authentication.

## 🛠 Tech Stack

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **PostgreSQL**
- **djangorestframework-simplejwt**
- **python-decouple (for environment variables)**

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend


2. Create Virtual Environment & Activate
python -m venv env
source env/bin/activate       # On Linux/Mac
env\Scripts\activate          # On Windows


3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432


5. Apply Migrations
python manage.py makemigrations
python manage.py migrate


6. Create Superuser (Optional)
python manage.py createsuperuser


7. Run the Server
python manage.py runserver


