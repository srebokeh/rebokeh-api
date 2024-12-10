# Rebokeh

Rebokeh application.

## Features

- RESTful API architecture using Django REST Framework.
- Token-based Authentication (JWT or Session-based).


## Tech Stack

- **Backend**: Django 4.x, Django REST Framework
- **Database**: PostgreSQL (or SQLite for development)
- **Authentication**: JWT Authentication (or Session Authentication)
- **API Documentation**: Swagger / ReDoc


## Installation

Follow the steps below to set up the project locally.

### Prerequisites

- Python 3.9+
- pip
- PostgreSQL (optional, default is SQLite for development)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rebokeh.git


2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


pip install -r requirements.txt



5. Apply database migrations

python manage.py migrate


6. Create a superuser (optional)

python manage.py createsuperuser


python manage.py runserver


API Documentation
The project includes API documentation that is auto-generated using tools like Swagger or ReDoc. You can access the API documentation via the following URLs:

Swagger UI: /swagger/
ReDoc UI: /redoc/
For example:

http://localhost:8000/swagger/
http://localhost:8000/redoc/

