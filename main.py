import os

import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask import Blueprint
from dotenv import load_dotenv
from flask_migrate import Migrate

parser_bp = Blueprint('parser_bp', __name__)
excel_validation_bp = Blueprint('excel_validation_bp', __name__)

def creat_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(parser_bp, url_prefix='/parser')
    app.register_blueprint(excel_validation_bp, url_prefix='/validation')
    return app


db = SQLAlchemy()



class BasicTypeGraphic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_date = db.Column(db.String(32), nullable=True)
    hours = db.Column(db.String(32), nullable=True)


class CheckedTypeGraphic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(32), nullable=True)
    hours = db.Column(db.String(32), nullable=True)

if __name__ == "__main__":
    app = creat_app()
    app.run()
    load_dotenv()
