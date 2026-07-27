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

## 1. Clone Repository
```bash
git clone https://github.com/laraib-test/Shoppingcart.git
cd Shoppingcart
```
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

``
## Playwright Test Automation

This project uses **Playwright with Python** for end-to-end (E2E) testing to validate the functionality of the Django Shopping Cart application. Playwright provides reliable cross-browser automation with powerful features such as automatic waiting, screenshots, tracing, and HTML test reports.

### Installing Playwright

Create and activate a Python virtual environment, then install the required dependencies:

```bash
pip install playwright
pip install pytest pytest-playwright pytest-html
playwright install
```

To verify the installation:

```bash
playwright --version
```

Run the test suite using:

```bash
pytest tests -v
```

Generate an HTML test report:

```bash
pytest tests --html=reports/report.html --self-contained-html
```

---

## Page Object Model (POM)

This project follows the **Page Object Model (POM)** design pattern to improve the maintainability, readability, and scalability of the test automation framework. POM separates page-specific locators and actions from the test scripts, allowing tests to focus on business scenarios rather than UI implementation details.

The framework is organized with dedicated page classes such as:

- `BasePage` – Common browser actions and reusable methods.
- `HomePage` – Homepage navigation and interactions.
- `ProductPage` – Product selection and product-related actions.
- `PricePage` – Product price management and updates.
- `CartPage` – Shopping cart operations.


