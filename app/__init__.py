from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app,db)

from app import routes