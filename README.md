# Django Cards API

A simple REST-style API built with Django to manage Pokémon cards.

## Features
- List all cards
- Retrieve a card by ID
- Filter cards by grade (e.g. `/cards/?grade=10`)
- SQLite database
- JSON responses

## Tech Stack
- Python
- Django
- SQLite

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/django-cards-api.git
cd django-cards-api
```
Create a virtual environment:
```
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Run migrations:
```
python manage.py migrate
```

Start the development server:
```
python manage.py runserver
```

## Endpoints

Get all cards
```
GET /cards/
```

Get card by ID
```
GET /cards/{id}/
```

Filter by grade
```
GET /cards/?grade=10
```

Example Response
```
[
  {
    "id": 1,
    "name": "Pikachu",
    "grade": 10
  }
]
```
