# Quick Overview

System with Django, Django Rest framework with SQLite database that have the following features:
      - User registration
      - User login   
      - Each user could create multiple products and get them
      - All users could retrieve products data

Rest APIs endpoints for:
      - Registration
      - Login
      - Create product and attach user to it (product fields are: name, price, seller)
      - Get products and the query should:
          - Filter by user
          - Order by price

## Built With

- Django 
- Django Rest Framework

## Running the code

- run:
    docker-compose up
- run for first time only:
    docker-compose run web python3 manage.py migrate


## API endpoints
Description of every endpoint in the API.

| resource                    | description                       |
|:----------------------------|:----------------------------------|
| `POST : /auth/signup/`               | register a user using POST request |
| `POST : /auth/login/`          | login with username and password |
| `POST : /products`        | create new product |
| `GET : /products/?seller=sellerUsername&order=ASC`        | list all products (use filter parameters are optional, use ASC for Ascending order py price and DESC for Descending order py price) |
