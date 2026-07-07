from flask import Blueprint
from flask import current_app as app 


view = Blueprint("view" , __name__)

@view.route("/")
def index():
    return "Hello from views"