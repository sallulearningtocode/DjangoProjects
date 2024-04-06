Django Shop Registration System Documentation
Introduction
This documentation outlines the functionalities of the Django Shop Registration System. This system allows users to register shops and search for shops based on their location.

Functionalities
1. Index Page
Description: Displays information about the application.
URL: /
Method: GET

2. Shop Registration
Description: Allows users to register shops with their details including name, latitude, and longitude.
URL: /registershop/
Methods:
GET: Renders the registration form.
POST: Handles form submission and saves shop details to the database.

3. Shop Search
Description: Enables users to search for nearby shops based on their current location.
URL: /search/
Methods:
GET: Renders the search form.
POST: Handles form submission, calculates distances between user location and registered shops using the Haversine formula, and returns a sorted list of nearby shops.


Installation and Usage
For installation instructions and usage guidelines, please refer to the provided README.md file.

API Documentation
The API documentation is available at /swagger/ endpoint.


Dependencies
Django
Django Rest Framework
drf-yasg