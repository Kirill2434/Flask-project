from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from app.comerce_parser.views import parser_bp
from app.excel_validation.views import validation_bp
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(parser_bp, url_prefix='/parser')
app.register_blueprint(validation_bp, url_prefix='/validation')

app.run()
load_dotenv()
