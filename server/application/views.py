from flask import Blueprint , request
from flask import current_app as app 
from werkzeug.security import generate_password_hash , check_password_hash
from application.models import db , Venue
from flask_security import login_user,auth_required, roles_required



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
    roles = [role.name for role in user.roles]
    return {"token" : token , "roles": roles}, 200


@view.route("/venue/create" , methods = ['POST'])
@auth_required("token")
@roles_required("admin")
def create_venue():
    name = request.json.get("name" , "")
    place = request.json.get("place")
    
    if not name:
        return {"error": "Invalid name" }, 404
    
    if not place:
        return {"error": "Invalid place" }, 404
    
    venue = Venue(name = name , place = place)
    db.session.add(venue)
    db.session.commit()
    
    return {"message": "Venue created successfully"}, 201


@view.route('/venue/search' , methods = ['POST'])
@auth_required("token")
@roles_required("admin")
def venue_search():
    search = request.json.get("search", "").strip()
    search.replace(" ", "")
    option = request.json.get("option")
    
    
    if (option not in ["Place" , "Name"]):
        return {"error" : "Invalid filter"} , 400
    
    if(option == "Place"):
        venues = Venue.query.filter(Venue.place.like(f"%{search}%")).all()
    else:
        venues = Venue.query.filter(Venue.name.like(f"%{search}%")).all()
        
    if (not venues):
        return {"error" : "No match found"} , 400
        
    
    
    return [{"id" : venue.id , 
            "name": venue.name, 
            "place" : venue.place} for venue in venues] , 200


@view.route("/venue/<int:id>/edit", methods=["POST"])
@auth_required("token")
@roles_required("admin")
def edit_venue(id):

    venue = Venue.query.get(id)

    if not venue:
        return {"error": "Venue not found"}, 404

    name = request.json.get("name", "").strip()
    place = request.json.get("place", "").strip()

    if not name:
        return {"error": "Invalid name"}, 400

    if not place:
        return {"error": "Invalid place"}, 400

    venue.name = name
    venue.place = place

    db.session.commit()
    

    return {
        "message": "Venue updated successfully",
        "venue": {
            "id": venue.id,
            "name": venue.name,
            "place": venue.place
        }
    }, 200