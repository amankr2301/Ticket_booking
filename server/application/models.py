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
    
    roles = db.relationship("Role" , 
                            secondary = "user_roles" , 
                            backref = db.backref("backref" , lazy = True))
    
class Role(db.Model , RoleMixin):
    __tablename__ = "role"
    
    id = db.Column(db.Integer() , primary_key = True)
    name = db.Column(db.String() , nullable = False)
    
    
class UserRoles(db.Model):
    __tablename__ = "user_roles"
    
    id = db.Column(db.Integer() , primary_key = True)
    user_id = db.Column(db.Integer() , db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer() , db.ForeignKey("role.id"))

class Venue(db.Model):
    __tablename__ = "venue"
    
    id = db.Column(db.Integer() , primary_key = True)
    name = db.Column(db.String() , nullable = False)
    place = db.Column(db.String() , nullable = False)

class Movie(db.Model):
    __tablename__ = "movie"
    
    id = db.Column(db.Integer() , primary_key = True)
    title = db.Column(db.String() , nullable = False)
    rating = db.Column(db.Integer())
    poster = db.Column(db.String())
    

class Genre(db.Model):
    __tablename__ = "genre"
    
    id = db.Column(db.Integer() , primary_key = True)
    type = db.Column(db.String() , nullable = False)

class MovieGenre(db.Model):
    __tablename__ = "movie_genre"
    
    id = db.Column(db.Integer() , primary_key = True)
    movie_id = db.Column(db.Integer() , db.ForeignKey("movie.id"))
    genre_id = db.Column(db.Integer() , db.ForeignKey("genre.id"))

class Show(db.Model):
    __tablename__ = "show"
    
    id = db.Column(db.Integer() , primary_key = True)
    movie_id = db.Column(db.Integer() , db.ForeignKey("movie.id"))
    venue_id = db.Column(db.Integer() , db.ForeignKey("venue.id"))
    capacity = db.Column(db.Integer() , nullable = False)
    price = db.Column(db.Integer() , nullable = False)
    start = db.Column(db.Integer() , nullable = False)
    end = db.Column(db.Integer() , nullable = False)

class ShowTiming(db.Model):
    __tablename__ = "show_timing"
    
    id = db.Column(db.Integer() , primary_key = True)
    show_id = db.Column(db.Integer() , db.ForeignKey("show.id"))
    time = db.Column(db.Time() , nullable = False)


class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer() , primary_key = True)
    show_id = db.Column(db.Integer() , db.ForeignKey("show.id"))
    user_id = db.Column(db.Integer() , db.ForeignKey("user.id"))
    tickets = db.Column(db.Integer() , nullable = False)


    







    
    
    

    
    
    
    
    
    