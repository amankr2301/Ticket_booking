from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin , RoleMixin


db = SQLAlchemy()

class User(db.Model , UserMixin):
    __tablename__ = "user"
    
    id = db.Column(db.Integer() , primary_key = True)
    first_name = db.Column(db.String() , nullable = False)
    last_name = db.Column(db.String())
    email = db.Column(db.String() , nullable = False , unique = True)
    password = db.Column(db.String() , nullable = False)
    active = db.Column(db.Boolean())
    authenticated = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(64) , unique = True , nullable = False) ##A unique internal identifier required by modern Flask-Security for authentication-related operations.
    
    
class Role(db.Model , RoleMixin):
    __tablename__ = "role"
    
    id = db.Column(db.Integer() , primary_key = True)
    name = db.Column(db.String() , nullable = False)
    
class UserRoles(db.Model):
    __tablename__ = "user_roles"
    
    id = db.Column(db.Integer() , primary_key = True)
    user_id = db.Column(db.Integer() , db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer() , db.ForeignKey("role.id"))
    
    
    

    
    
    
    
    
    