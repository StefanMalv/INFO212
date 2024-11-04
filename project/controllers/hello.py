from project import app
from flask import render_template, request, redirect, url_for
import project.models.User as user

# Customer Car methods
@app.route("/order_car", methods=["POST"])
def index_order_car():
    car_id = request.form["car_id"]
    customer_id = request.form["customer_id"]
    
    if request.method == "POST":
        try:   
           user.order_car(car_id, customer_id)
           
        except:
                return "Could not order car"

@app.route("/cancel_car", methods=["PUT"])
def index_cancel_order():
    cancel_car_id = request.form["car_id"]
    cancel_customer_id = request.form["customer_id"]
    
    if request.method == "PUT":
        try:   
           user.cancel_order_car(cancel_car_id, cancel_customer_id)
           
        except:
                return "Could not cancel order"
            
@app.route("/rent_car", methods=["POST"])
def index_rent_car():
    rent_car_id = request.form["car_id"]
    rent_customer_id = request.form["customer_id"]
    
    if request.method == "POST":
        try:    
            user.rent_car(rent_car_id, rent_customer_id)
        
        except:
            return "Could not rent car"
        
@app.route("/return_car", methods=["POST"])
def index_return_car():
    rent_car_id = request.form["car_id"]
    rent_customer_id = request.form["customer_id"]
    
    if request.method == "POST":
        try:
            user.return_car(rent_car_id, rent_customer_id)
        
        except:
            return "Could not return car"
        
# Car methods
@app.route("/create_car", methods=["POST"])
def index_create_car():
    car_brand_create = request.form["brand"]
    car_model_create = request.form["model"]
    car_year_create = request.form["year"]
    car_location_create = request.form["location"]
    
    if request.method == "POST":
        try:
            user.create_car(car_brand_create, car_model_create, car_year_create, car_location_create)
        
        except:
            return "Could not create car"

@app.route("/read_car", methods=["GET"])
def index_read_car():
    car_id_read = request.form["car_id"]
    
    if request.method == "POST":
        try:
            user.read_car(car_id_read)
        
        except:
            return "Could not return car"

@app.route("/delete_car", methods=["POST"])
def index_delete_car():
    car_id_delete = request.form["employee_id"]
    
    if request.method == "POST":
        try:
            user.delete_car(car_id_delete)
        
        except:
            return "Could not delete employee"
        
@app.route("/update_car", methods=["POST"])
def index_update_car():
    car_id_update = request.form["car_id"]
    car_brand_update = request.form["brand"]
    car_model_update = request.form["model"]
    car_year_update = request.form["year"]
    car_location_update = request.form["location"]
    car_status_update = request.form["status"]

    
    if request.method == "POST":
        try:
            user.update_car(car_id_update, car_brand_update, car_model_update, car_year_update, car_location_update, car_status_update)
        
        except:
            return "Could not update car"
        

# Employee methods        
@app.route("/create_emploee", methods=["POST"])
def index_create_employee():
    employee_name = request.form["name"]
    employee_adress = request.form["adress"]
    employee_branch = request.form["branch"]
    
    if request.method == "POST":
        try:
            user.create_employee(employee_name, employee_adress, employee_branch)
        
        except:
            return "Could not create employee"


@app.route("/read_employee", methods=["GET"])
def index_read_employee():
    employee_id = request.form["employee_id"]
    
    if request.method == "POST":
        try:
            user.read_employee(employee_id)   
        except:
            return "Could not read employee"

@app.route("/delete_employee", methods=["POST"])
def index_delete_employee():
    employee_delete = request.form["employee_id"]
    
    if request.method == "POST":
        try:
            user.delete_employee(employee_delete)
        
        except:
            return "Could not delete employee"
        
@app.route("/update_employee", methods=["POST"])
def index_update_employee():
    update_id_emoloyee = request.form["id"]
    update_name_emoloyee = request.form["name"]
    update_adress_employee = request.form["adress"]
    update_branch_employee = request.form["branch"]

    
    if request.method == "POST":
        try:
            user.update_employee(update_id_emoloyee, update_name_emoloyee, update_adress_employee, update_branch_employee)
        
        except:
            return "Could not update employee"
        
# Customer methods
@app.route("/create_customer", methods=["POST"])
def index_create_customer():
    create_name_customer = request.form["name"]
    create_age_customer = request.form["age"]
    create_adress_customer = request.form["adress"]
    
    if request.method == "POST":
        try:
            user.create_customer(create_name_customer, create_age_customer, create_adress_customer)
        
        except:
            return "Could not create customer"
        
@app.route("/read_customer", methods=["POST"])
def index_read_customer():
    read_id_customer = request.form["customer_id"]
    
    
    if request.method == "POST":
        try:
            user.read_customer(read_id_customer)
        
        except:
            return "Could not read customer"
        
@app.route("/update_customer", methods=["POST"])
def index_update_customer():
    update_id_customer = request.form["customer_id"]
    update_name_customer = request.form["name"]
    update_age_customer = request.form["age"]
    update_adress_customer = request.form["adress"]
    
    if request.method == "POST":
        try:
            user.update_customer(update_id_customer, update_name_customer, update_age_customer, update_adress_customer)
        
        except:
            return "Could not return customer"
        
@app.route("/delete_customer", methods=["POST"])
def index_delete_customer():
    delete_id_customer = request.form["customer_id"]
    
    
    if request.method == "POST":
        try:
            user.read_customer(delete_id_customer)
        
        except:
            return "Could not delete customer"
        
