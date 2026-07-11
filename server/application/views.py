from flask import Blueprint , request
from flask import current_app as app 
from werkzeug.security import generate_password_hash , check_password_hash
from application.models import db
from flask_security import login_user



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


@view.route("/signin" , methods = ['POST'])
def signin():
    email = request.json.get("email")
    password = request.json.get("password")
    
    user = app.security.datastore.find_user(email = email)
    if (not user or not check_password_hash(user.password , password)):
        return {"error": "Invalid email or password"}, 404
    
    login_user(user)
    token = user.get_auth_token()
    return {"token" : token}, 200
    
    

    
    