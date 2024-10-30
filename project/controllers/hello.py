from project.templates import app
from flask import render_template, request, redirect, url_for
import project.models.User as user


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
        