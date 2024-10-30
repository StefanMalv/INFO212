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


def order_car(car_id, customer_id):
    data = _get_connection().execute_query("MATCH (a:$car_id {car_id} c:$customer_id {customer_id})")
    pass
    
class Employee:
    
    def __init__(self, name, adress, branch):
        self.name = name 
        self.adress = adress
        self.branch = branch
        self.id = random.randint(999, 9999)

def create_employee(name, adress, branch):
    new_employee = Employee(name, adress, branch)
    
    employee = _get_connection().execute_query("MERGE (a:Employee {name: $name, adress: $adress, branch: $branch, id: $id}) RETURN a;", 
                                        name=new_employee.name, adress=new_employee.adress, branch=new_employee.branch, id=new_employee.id)
    
    return employee, print("employee added to database")

# Get employee from database
def read_employee(employee_id):
    employee = _get_connection().execute_query("MATCH (a:Employee {id: $id}) RETURN a;", id=employee_id)
    return employee, print("employee found in database")
    

# Update existing values for employee in Database
def update_employee(employee_id, name, adress, branch):
    employee = _get_connection().execute_query("MATCH (a:Employee {id: $id}) SET a.name = $name, a.adress = $adress, a.branch = $branch RETURN a;", 
                                        id=employee_id, name=name, adress=adress, branch=branch)
    return employee, print("employee updated in database")


# Delete Employee from database
def delete_employee(employee_id):
    employee = _get_connection().execute_query("MATCH (a:Employee {id: $id}) DELETE a;", id=employee_id)
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

    car = _get_connection().execute_query("MERGE (a:Car {year: $year, location: $location, model: $model, id: $id, brand: $brand, status: $status}) RETURN a;", 
                                        year=new_car.year, location=new_car.location, model=new_car.model, id=new_car.id, brand=new_car.brand, status=new_car.status)

    return car, print("car added to database")

# Get car from database
def read_car(self):
    pass

# Update existing values for car in Database
def update_car(self):
    pass

# Delete car from database
def delete_car(self):
    pass
    
    
class Customer:
    
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
        self.id = random.randint(999, 9999)

# Create a new Customer and add to database
def create_customer(name, age, adress):
    
    new_customer = Customer(name, age, adress)
    
    customer = _get_connection().execute_query("MERGE (c:CUSTOMER {adress: $adress, name: $name, id: $id, age: $age}) RETURN c;",
                                               adress=new_customer.adress, name=new_customer.name, age=new_customer.age)
    return customer

# Get Customer from database
def read_customer():
    pass

# Update existing values for Customer in Database
def update_customer():
    pass

# Delete Customer from database
def delete_customer():
    pass

driver.close
