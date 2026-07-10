from flask import Blueprint , request
from flask import current_app as app 



view = Blueprint("view" , __name__)

@view.route("/")
def home():
    return "🚀 Flask backend is up and running successfully!"

@view.route("/signup", methods=["GET" , "POST"])
def signup():

    firstname = request.json.get("firstname")
    lastname = request.json.get("lastname")
    email = request.json.get("email")

    return firstname ; 

    
    