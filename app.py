from flask import Flask
from config import Config

#an flask instance to create a path to other files
app = Flask(__name__)
app.config.from_object(Config)