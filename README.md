# Grocery Shopping Django App

A simple Django-based Shopping Cart application that allows users to:

- Register and login
- Manage products
- Add prices from different stores
- Compare product prices
- Manage shopping lists

---

## Features

- User Authentication (Login/Register)
- Product Management
- Store Management
- Price Tracking
- Shopping List
- Clean Django Templates
- SQLite Database
- Responsive UI

---

## Technologies Used

- Python 3
- Django 6
- HTML
- CSS
- SQLite

---

## Project Structure

Shoppingcart/
│
├── manage.py
├── requirements.txt
├── .gitignore
│
├── shoppingcart/
│
├── shoppinglist/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
│
└── venv/

---
## Installation

### 1. Clone Repository
```bash
git clone https://github.com/laraib-test/Shoppingcart.git
cd Shoppingcart

## Create Virtual Environment
python -m venv venv

## Activate environment:
venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Run Migrations
python manage.py migrate

## Start Development Server
python manage.py runserver
## Open browser:
http://127.0.0.1:8007/
## Create Superuser
python manage.py createsuperuser
Open browser
git clone https://github.com/laraib-test/Shoppingcart.git
cd Shoppingcart
