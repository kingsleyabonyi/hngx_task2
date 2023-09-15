# HNGx CRUD Person REST API

This is a Django REST API project that allows you to manage and interact with a "Person" resource. You can perform CRUD (Create, Read, Update, Delete) operations on individuals' data.
# Table of Contents

    Getting Started
    Prerequisites
    Installation
    Usage
    API Endpoints
    Testing
    Deployment
    Documentation
    Contributing
    License

# Getting Started

UML Diagram for the CRUD Person REST API
Prerequisites

    Python (3.10 or higher)
    Django (3.0 or higher)
    Django Rest Framework
    Git

Installation

    Clone the repository:

git clone https://github.com/Tomilola-ng/TrackBackendTask2.git
cd my-awesome-api

    Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate

    Install dependencies:

pip install -r requirements.txt

    Apply database migrations:

python manage.py migrate

    Start the development server:

python manage.py runserver

Your API should now be running locally at http://localhost:8000/.
Usage

To use the API, you can make HTTP requests to the provided endpoints. Here's an overview of the available endpoints:
API Endpoints

    POST /api: Create a new person.
    GET /api/<user_id>: Retrieve details of a person by their ID.
    PUT /api/<user_id>: Update details of an existing person.
    DELETE /api/<user_id>: Remove a person.

Example Requests

    Create a new person:

POST http://localhost:8000/api
Content-Type: application/json
{
"name": "John Doe",
"email": "john@example.com"
}

    Retrieve details of a person:

GET http://localhost:8000/api/1

    Update details of a person:

PUT http://localhost:8000/api/1
Content-Type: application/json
{
"name": "Updated John Doe",
"email": "updated_john@example.com"
}

    Remove a person:

DELETE http://localhost:8000/api/1

Testing

To run the test suite, use the following command:

python manage.py test

Documentation

For detailed information on how to use this API, check the API Documentation file.
