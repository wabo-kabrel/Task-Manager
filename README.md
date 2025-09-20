# Task Manager API
A simple **Task Management API** built with **Django** and **Django REST Framework (DRF)**.
This project demonstrates user-friendly CRUD operations (Create, Read, Update, Delete) via RESTful APIs.

## Features
- Create, list, update and delete tasks.
- RESTful API endpoints (JSON responses).
- Powered by Django 5 and DRF.
- PostgreSQL support (optional, can run on SQLite for local dev).
- Easily extendable for authentication & frontend integration.


## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default), PostgreSQL (for production)
- **Tools:** Postman / curl for testing

## Project Structure
```bash
taskmanager/
│── taskmanager/        # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py         # Root URL config
│   └── wsgi.py
│── tasks/              # Task management app
│   ├── migrations/     # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py       # Task model
│   ├── tests.py
│   ├── urls.py         # API routes
│   ├── serializers.py  # DRF serializers
│   └── views.py        # API logic
│── accounts/           # User authentication app
│   ├── migrations/     # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py         # Authentication routes
│   └── views.py        # Registration, login, logout logic
│── manage.py           # Django entrypoint
│── requirements.txt    # Project dependencies
│── README.md           # Documentation
└── LICENSE             # MIT License
```

## Installation
**1. Clone the repository**
```bash
git clone https://github.com/wabo-kabrel/Task-Manager.git
cd taskmanager
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```
**4. (Optional) Update `taskmanager/settings.py` to use PostgreSQL**
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "taskmanager_db",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

**5. Run migrations**
```bash
python manage.py migrate
```

**6. Start the development server**
```bash
python manage.py runserver
```

## API Endpoints
### Base URL
```
http://127.0.0.1:8000/tasks/api/
```
### Endpoints

| Method | Endpoint           | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/tasks/api/`      | List all tasks        |
| POST   | `/tasks/api/`      | Create a new task     |
| GET    | `/tasks/api/<id>/` | Retrieve a task by ID |
| PUT    | `/tasks/api/<id>/` | Update a task by ID   |
| DELETE | `/tasks/api/<id>/` | Delete a task by ID   |

### Example Requests
#### Create a Task
```json
POST /tasks/api/
{
  "title": "Learn DRF",
  "completed": false
}
```
#### Response
```json
{
  "id": 1,
  "title": "Learn DRF",
  "completed": false
}
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.








