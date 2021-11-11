from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BasicTypeGraphic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_date = db.Column(db.String(32), nullable=True)
    hours = db.Column(db.String(32), nullable=True)


class CheckedTypeGraphic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(32), nullable=True)
    hours = db.Column(db.String(32), nullable=True)