# Finance Tracker

A Django personal finance tracker that allows users to manage income, expenses, budgets, and recurring transactions.

## Features

- User authentication
- Add, edit and delete transactions
- Categories
- Budget management
- Balance calculation
- Currency conversion
- REST API using Django REST Framework
- Recurring transactions
- Bootstrap responsive interface

## Technologies

- Python
- Django
- Django REST Framework
- Bootstrap 5
- SQLite
- HTML/CSS

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/finance-tracker.git
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Create a `.env`

```
SECRET_KEY=your_secret_key
DEBUG=True
EXCHANGE_API_URL=https://api.exchangerate-api.com/v4/latest/GEL
```

Run migrations

```bash
python manage.py migrate
```

Start server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

POST `/api/auth/register/`

POST `/api/auth/login/`

POST `/api/auth/refresh/`

### Transactions

GET `/api/transactions/`

POST `/api/transactions/`

GET `/api/transactions/<id>/`

PUT `/api/transactions/<id>/`

DELETE `/api/transactions/<id>/`

### Categories

GET `/api/categories/`

### Balance

GET `/api/balance/`

### Budgets

GET `/api/budgets/`

### Currency Conversion

GET `/api/convert/?amount=100&to=USD`

## Recurring Transactions

Supports

- Daily
- Weekly
- Monthly

Monthly recurrence implements assignment Variant 1:

If the day does not exist in the next month (for example January 31 → February), the occurrence is moved to the **1st day of the month**.

## Author

Your Name