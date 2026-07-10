from flask import Blueprint , request
from flask import current_app as app 
from werkzeug.security import generate_password_hash
from application.models import db



view = Blueprint("view" , __name__)

@view.route("/")
def home():
    return "🚀 Flask backend is up and running successfully!"

@view.route("/signup", methods=["POST"])
def signup():

    firstname = request.json.get("firstname")
    lastname = request.json.get("lastname")
    email = request.json.get("email")
    password = request.json.get("password")
    confirm = request.json.get("confirm")

    if app.security.datastore.find_user(email = email):
        return {"error" : "Email already exists"} , 400 
    

    user = app.security.datastore.create_user(first_name = firstname , last_name = lastname , email = email , 
                           password = generate_password_hash(password))
    role = app.security.datastore.find_role("user")
    app.security.datastore.add_role_to_user(user , role)

    db.session.commit()

    return {"message" : "registration successfull"} , 201   

    
    