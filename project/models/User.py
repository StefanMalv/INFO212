from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
import random

URI = "neo4j+ssc://b41618ba.databases.neo4j.io"
AUTH = ("neo4j", "kXhTM8agdagzrvztaIDVKYRFdA6KEohr77HM8UUZLRo")

def _get_connection() -> Driver:
    print("Establishing connection to the database...")
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    print("Connection established")
    return driver

try:
    driver = _get_connection()
    print("Connection successful")
except Exception as e:
    print(f"Error: {str(e)}")

# Orders a car for a customer, if the car is available
def order_car(car_id, customer_id):
    car = _get_connection().execute_query(
        "MATCH (c:Car {id: $car_id}) RETURN c;", car_id=car_id
        )
    customer = _get_connection().execute_query(
        "MATCH (c:Customer {id: $customer_id}) RETURN c;", customer_id=customer_id
        )
    
    # Check if the customer has already booked another car
    existing_order = _get_connection().execute_query(
        "MATCH (customer:Customer {id: $customer_id})-[:ORDERED]->(c:Car) RETURN c;", customer_id=customer_id
        )
    
    if existing_order:
        return None, "Customer has already booked another car"
    
    if car['status'] == 'available':
        order = _get_connection().execute_query(
            "MATCH (c:Car {id: $car_id}) "
            "SET c.status = 'booked' "
            "MERGE (customer:Customer {id: $customer_id})-[:ORDERED]->(c) "
            "RETURN c;", car_id=car_id, customer_id=customer_id
            )
        return order, print("Car ordered by customer")
    else:
        return None, print("Car is not available")

# Cancels an order for a car by a customer
def cancel_order_car(car_id, customer_id):
    # Check if the customer has booked the car
    existing_order = _get_connection().execute_query(
        "MATCH (customer:Customer {id: $customer_id})-[:ORDERED]->(c:Car {id: $car_id}) RETURN c;", customer_id=customer_id, car_id=car_id
        )
    
    if existing_order:
        _get_connection().execute_query(
            "MATCH (customer:Customer {id: $customer_id})-[r:ORDERED]->(c:Car {id: $car_id}) " 
            "SET c.status = 'available' "
            "DELETE r " 
            "RETURN c;", customer_id=customer_id, car_id=car_id
            )
        return "Order cancelled and car is now available"
    else:
        return "No such order found"
    
# Rents a car for a customer, if the customer has a booking for the car
def rent_car(car_id, customer_id):
    # Check if the customer has booked the car
    existing_order = _get_connection().execute_query(
        "MATCH (customer:Customer {id: $customer_id})-[:ORDERED]->(c:Car {id: $car_id}) RETURN c;", 
        customer_id=customer_id, car_id=car_id
        )
    
    if existing_order:
        _get_connection().execute_query(
            "MATCH (customer:Customer {id: $customer_id})-[r:ORDERED]->(c:Car {id: $car_id}) "
            "SET c.status = 'rented' "
            "DELETE r "
            "MERGE (customer)-[:RENTED]->(c) "
            "RETURN c;", customer_id=customer_id, car_id=car_id
            )
        return "Car rented by customer"
    else:
        return "No booking found for this car"
    
# Returns a rented car by a customer
def return_car(car_id, customer_id, car_status):
    # Check if the customer has rented the car
    existing_rental = _get_connection().execute_query(
        "MATCH (customer:Customer {id: $customer_id})-[:RENTED]->(c:Car {id: $car_id}) RETURN c;", 
        customer_id=customer_id, car_id=car_id
        )
    
    if existing_rental:
        _get_connection().execute_query(
            "MATCH (customer:Customer {id: $customer_id})-[r:RENTED]->(c:Car {id: $car_id}) "
            "SET c.status = $car_status "
            "DELETE r "
            "RETURN c;", customer_id=customer_id, car_id=car_id, car_status=car_status
            )
        return "Car returned and status updated"
    else:
        return "No rental found for this car"
    
class Employee:
    
    def __init__(self, name, adress, branch):
        self.name = name 
        self.adress = adress
        self.branch = branch
        self.id = random.randint(999, 9999)

def create_employee(name, adress, branch):
    new_employee = Employee(name, adress, branch)
    
    employee = _get_connection().execute_query(
        "MERGE (a:Employee {name: $name, adress: $adress, branch: $branch, id: $id}) RETURN a;", 
        name=new_employee.name, adress=new_employee.adress, branch=new_employee.branch, id=new_employee.id
        )
    
    return employee, print("employee added to database")

# Get employee from database
def read_employee(employee_id):
    employee = _get_connection().execute_query(
        "MATCH (a:Employee {id: $id}) RETURN a;", id=employee_id
        )
    return employee, print("employee found in database")
    

# Update existing values for employee in Database
def update_employee(employee_id, name, adress, branch):
    employee = _get_connection().execute_query(
        "MATCH (a:Employee {id: $id}) SET a.name = $name, a.adress = $adress, a.branch = $branch RETURN a;", 
        id=employee_id, name=name, adress=adress, branch=branch
        )
    return employee, print("employee updated in database")


# Delete Employee from database
def delete_employee(employee_id):
    employee = _get_connection().execute_query(
        "MATCH (a:Employee {id: $id}) DELETE a;", id=employee_id
        )
    return employee, print("employee deleted from database")
    

class Car:
    
    def __init__(self, brand, model, year, location, status=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.location = location
        self.id = random.randint(999, 9999)
        self.status = status

# Create a new car and add to database
# Seminar leader sin kode
def create_car(brand, model, year, location):
    new_car = Car(brand, model, year, location)

    car = _get_connection().execute_query(
        "MERGE (a:Car {year: $year, location: $location, model: $model, id: $id, brand: $brand, status: $status}) RETURN a;", 
        year=new_car.year, location=new_car.location, model=new_car.model, id=new_car.id, brand=new_car.brand, status=new_car.status
        )

    return car, print("car added to database")

# Get car from database by using car id
def read_car(self):
    car = _get_connection().execute_query(
        "MATCH (a:Car {id: $id}) RETURN a;", id=self.id
        )
    return car, print("car found in database")
   
# Update existing values for car in Database by searching for the car id
def update_car(id, brand, model, year, location, status):
    car = _get_connection().execute_query(
        "MATCH (a:Car {id: $id}) SET a.brand = $brand, a.model = $model, a.year = $year, a.location = $location , a.status = $status RETURN a;", 
        id=id, brand=brand, model=model, year=year, location=location, status=status
        )
    return car, print("car updated in database")

# Delete car from database by using car id
def delete_car(id):
    car = _get_connection().execute_query(
        "MATCH (a:Car {id: $id}) DELETE a;", id=id
        )
    return car, print("car deleted from database")
    
class Customer:
    
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
        self.id = random.randint(999, 9999)

# Create a new Customer and add to database
def create_customer(name, age, adress):

    new_customer = Customer(name, age, adress)
    
    customer = _get_connection().execute_query(
        "MERGE (c:CUSTOMER {adress: $adress, name: $name, id: $id, age: $age}) RETURN c;", 
        adress=new_customer.adress, name=new_customer.name, age=new_customer.age
        )
    return customer, print("customer added to database")

# Get Customer from database
def read_customer(id):
    customer = _get_connection().execute_query(
        "MATCH (c:Customer {id: $id}) RETURN c;", id=id
        )
    return customer, print("customer found in database")

# Update existing values for Customer in Database
def update_customer(id, name, age, adress):
    customer = _get_connection().execute_query(
        "MATCH (c:Customer {id: $id}) SET c.name = $name, c.age = $age, c.adress = $adress RETURN c;", 
        id=id, name=name, age=age, adress=adress
        )
    return customer, print("customer updated in database")

# Delete Customer from database
def delete_customer(id):
    customer = _get_connection().execute_query(
        "MATCH (c:Customer {id: $id}) DELETE c;", id=id
        )
    return customer, print("customer deleted from database")

# Close the connection
driver.close()
