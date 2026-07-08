from flask import Flask 
from flask_security import SQLAlchemyUserDatastore , Security


def create_app():
    from application.views import view
    from application.models import db , User , Role , UserRoles
    from werkzeug.security import generate_password_hash
    
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./model.db'
    app.config["SECRET_KEY"] = "JGOIHIGHOIRJI"

    
    db.init_app(app) 
    datastore = SQLAlchemyUserDatastore(db , User , Role)
    app.security = Security(app , datastore)
    
    app.register_blueprint(view)
    
    with app.app_context():
        db.create_all() 
        
        if not Role.query.all():
             
            admin = app.security.datastore.create_role(name = "admin")
            app.security.datastore.create_role(name = "user")
            db.session.flush()
            
            user = app.security.datastore.create_user(first_name = "aman" , 
                                            last_name = "kumar" , 
                                            email = "aman@example.com" , 
                                            password = generate_password_hash("aman123"))
            
            app.security.datastore.add_role_to_user(user , admin)
            
            db.session.commit()
        
        
    
    return app 

app = create_app()