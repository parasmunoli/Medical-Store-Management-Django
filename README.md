# Medical Store Management System
A web-based application developed using Django to streamline the management of medical store operations, including inventory control, sales tracking, and customer management.

## Features
- **User Authentication:** Secure login and registration system for administrators and staff.

- **Inventory Management:** Add, update, and delete medicine records with details like name, manufacturer, price, and quantity.

- **Sales Processing:** Record sales transactions, generate invoices, and update stock levels accordingly.

- **Customer Management:** Maintain customer information and purchase history.

- **Reporting:** Generate reports on sales, inventory status, and customer activity.

## Technologies Used
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite

## Installation and Setup
### Prerequisites
- Python 3.x
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Steps
1. **Clone the Repository**

```
git clone https://github.com/parasmunoli/Medical-Store-Management-Django.git
cd Medical-Store-Management-Django
```

2. **Create and Activate Virtual Environment (Optional)**

```
python -m venv env
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```
3. **Install Dependencies**

```
pip install -r requirements.txt
```
4. **Apply Migrations**
```
python manage.py makemigrations
python manage.py migrate
```
5. **Create Superuser**

```
python manage.py createsuperuser
```
6. **Run the Development Server**

```
python manage.py runserver
```
7. **Access the Application**

Open your web browser and navigate to http://127.0.0.1:8000/ to use the application.

## Project Structure

```
Medical-Store-Management-Django/
├── medstore/            # Main Django project directory
├── pharma/              # Django app for managing pharmacy operations
├── db.sqlite3           # SQLite database file
├── manage.py            # Django management script
└── requirements.txt     # List of project dependencies
```
