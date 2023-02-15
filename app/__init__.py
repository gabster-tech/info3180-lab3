from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config) #adds the configuration values to your Flask app.config
mail = Mail(app) #initializing Flask_Mail
from app import views