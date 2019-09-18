from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


app = Flask(__name__)

app.debug = True
app.config.from_object(Config)

from app import routes
bootstrap = Bootstrap(app)

