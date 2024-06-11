# blog_api
# Overview
This project is a simple RESTful API for a blogging platform that allows users to create, read, update, and delete blog posts. It also includes user registration and login with JWT-based authentication.

# Features
CRUD operations for blog posts (GET, POST, PUT, DELETE)
User registration and login
JWT-based authentication
Basic validation for input data
Secure against common vulnerabilities like SQL injection
# Tech Stack
Backend Framework: Flask
Database: PostgreSQL
Authentication: JSON Web Tokens (JWT)
ORM: SQLAlchemy
# Setup and Installation
# Prerequisites
Python 3.x
PostgreSQL
Git

# Installation Steps
Clone the repository:
> git clone https://github.com/Kj-kja/blog_api.git
> cd blog-api

Create a virtual environment and activate it:
> python -m venv venv
> venv\Scripts\activate  # On Windows

Install the required dependencies:
 > pip install -r requirements.txt

Set up PostgreSQL:
Create a new PostgreSQL database.
Update the config.py file with your database credentials.

Run database migrations:
> flask db upgrade

Run the application:
> python app.py


