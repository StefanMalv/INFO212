# About this project
This project is a Car Rental Management System developed as part of the INFO212 course at the University of Bergen. The purpose of this project is to provide a functional car rental management solution, allowing users to perform operations such as ordering, renting, and returning cars, along with managing car, customer, and employee data. The system is built using Flask, Neo4j, and Python.

# Car Rental Management System

This is a Car Rental Management System built using Flask, Neo4j, and Python. The system allows customers to order, rent, and return cars, manage CRUD operations on cars, customers, and employees, and interact with the database to retrieve and update car rental information.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Endpoints](#endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
project/
├── app.py                   # Flask application setup
├── models/
│   └── User.py              # Contains functions for car order, rental, and return processes
├── main.py                  # Main application entry point
└── README.md                # Project documentation (this file)
```

## Features

- **Order a Car**: Allows customers to place an order for a car if available.
- **Cancel Order**: Allows customers to cancel an existing car order.
- **Rent a Car**: Allows customers to rent a car they've previously ordered.
- **Return a Car**: Allows customers to return a rented car and update its status.
- **CRUD Operations**:
  - **Car Management**: Create, read, update, and delete cars in the database.
  - **Customer Management**: Create, read, update, and delete customer information.
  - **Employee Management**: Create, read, update, and delete employee information.

## Endpoints

### Car Operations

- **Order a Car**: `POST /order-car`
- **Cancel Order**: `POST /cancel-order-car`
- **Rent a Car**: `POST /rent-car`
- **Return a Car**: `POST /return-car`

### CRUD Operations

- **Car CRUD**:
  - Create Car: `create_car()`
  - Read Car: `read_car()`
  - Update Car: `update_car()`
  - Delete Car: `delete_car()`

- **Customer CRUD**:
  - Create Customer: `create_customer()`
  - Read Customer: `read_customer()`
  - Update Customer: `update_customer()`
  - Delete Customer: `delete_customer()`

- **Employee CRUD**:
  - Create Employee: `create_employee()`
  - Read Employee: `read_employee()`
  - Update Employee: `update_employee()`
  - Delete Employee: `delete_employee()`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/StefanMalv/INFO212.git
   cd car-rental-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Neo4j**:
   - Ensure Neo4j is running and accessible.
   - Update `URI` and `AUTH` in the code with your Neo4j credentials.

4. **Run the Application**:
   ```bash
   python main.py
   ```

   The application will start at `http://127.0.0.1:5000`.

## Usage

- Use any API client (like [Postman](https://www.postman.com/)) to send requests to the endpoints.
- For each endpoint, provide the necessary data:
  - `car_id`, `customer_id` for most operations.
  - `status` for `return_car`.
- Example of a POST request to order a car:
  ```http
  POST /order-car
  Content-Type: application/json
  {
      "car_id": "123",
      "customer_id": "456"
  }
  ```

## Dependencies

- **Flask**: Web framework for Python.
- **Neo4j**: Graph database to manage car, customer, and employee data.
- **neo4j-driver**: Official driver for connecting to Neo4j from Python.



This README provides a basic overview of the Car Rental Management System, including installation steps, features, and usage instructions.

