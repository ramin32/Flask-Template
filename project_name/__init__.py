from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('settings')

db = SQLAlchemy(app)

import project_name.views
import project_name.models
