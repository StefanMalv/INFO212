from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

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
    
    employee_count = 0
    
    def __init__(self, name, adress, branch, id):
        self.name = name 
        self.adress = adress
        self.branch = branch
        self.id = id


    # Create a new employee and add to database
    def create_employee(self, name, adress, branch):
        
        new_employee_id = self.employee_count
        
        new_employee = Employee(name, adress, branch, new_employee_id)
        
        return new_employee
    
    # Get employee from database
    def read_employee(self):
        pass
    
    # Update existing values for employee in Database
    def update_employee(self):
        pass
    
    # Delete Employee from database
    def delete_employee(self):
        pass
        

class Car:
    
    car_count = 0
    
    def __init__(self, brand, model, year, location, id, status=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.loction = location
        self.id = id
        self.status = status

    # Create a new car and add to database
    def create_car(self, brand, model, year, location):
        new_car_id = self.car_count
        
        new_car = Car(brand, model, year, location, new_car_id)
        
        return new_car
    
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
    
    customer_count = 0
    
    def __init__(self, name, age, adress, id):
        self.name = name
        self.age = age
        self.adress = adress
        self.id = id

    # Create a new Customer and add to database
    def create_customer(self, name, age, adress):
        new_customer_id = self.customer_count
        
        new_customer = Customer(name, age, adress, new_customer_id)
        
        return new_customer
    
    # Get Customer from database
    def read_customer(self):
        pass
    
    # Update existing values for Customer in Database
    def update_customer(self):
        pass
    
    # Delete Customer from database
    def delete_customer(self):
        pass


# main function for createing objects
def create_main(object_type, object):
    pass

#main function for deleteing one of the three object 
def delete_main(object_type, object):
    
    if type(object_type) is type(Customer):
        # remove Customer from database
        pass
    
    if type(object_type) is type(Car):
        # remove Car from database
        pass
    
    if type(object_type) is type(Employee):
        # remove Employee from database
        pass


driver.close()