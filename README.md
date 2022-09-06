# Django Python Api Backend

## How to start

Clone or Fork the repository:

     git clone https://github.com/diogowernik/fii_infra_backend backend

Create the python environment:

    python3 -m venv backend_env
    source backend_env/bin/activate
    cd backend
    python3 -m pip install -r requirements.txt

Migrate the database:

    python manage.py migrate

Create the superuser:

    python manage.py createsuperuser

Run the server:

    python manage.py runserver

Go to running application:

    http://localhost:8000/

Login to the admin:

    http://localhost:8000/admin/

## Features and Things to do

This app is not ready, there are some features that are missing. And some features that are working.

### Features that are Working for users on the backend

- frontend

### Features that need to be done for users on the backend

- sync with frontend

### Features that are Working for admin

- Admin
