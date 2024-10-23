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


    # Create a new employee and add to database
def create_employee(name, adress, branch):
    new_employee = Employee(name,  adress, branch)
    query = "MERGE (e:EMPLOYEE {name: $name, adress: $adress, branch: $branch id: $id}) RETURN e;"
    try:
        data = _get_connection().execute_query(query, 
                name=new_employee.name, adress=new_employee.adress, branch=new_employee.branch, id=new_employee.id)
    except:
        print("Fuck me!!!!!")

# Seminar leader sin kode
def save_car(make, model, reg, year, capacity, location, status):
    cars = _get_connection().execute_query("MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, capacity:$capacity, location:$location, status:$status}) RETURN a;", make = make, model = model, reg = reg, year = year, capacity = capacity, location = location, status = status)

# Get employee from database
def read_employee():
    pass

# Update existing values for employee in Database
def update_employee():
    pass

# Delete Employee from database
def delete_employee():
    pass
        

class Car:
    
    def __init__(self, brand, model, year, location, status=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.loction = location
        self.id = random.randint(999, 9999)
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
    
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
        self.id = random.randint(999, 9999)

    # Create a new Customer and add to database
    def create_customer(self, name, age, adress):
        
        new_customer = Customer(name, age, adress)
        
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

create_employee("Lars", "No", "HR")
driver.close()