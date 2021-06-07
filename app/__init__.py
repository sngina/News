from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap

def create_app (config_name):

    app = Flask (__name__) 

    #setting up configuration
    app.config.from_object(config_options[config_name])


    #initialzing Flask Extensions
    bootstrap = Bootstrap(app)

    #registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting congif
    from .request import configure_response 
    configure_response(app)
 
    return app 