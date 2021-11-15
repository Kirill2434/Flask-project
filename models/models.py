from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BasicTypeGraphic(db.Model):
    main_date = db.Column(db.String(999), primary_key=True, nullable=True, unique=True)
    hours = db.Column(db.String(999), nullable=True)


class CheckedTypeGraphic(db.Model):
    date = db.Column(db.String(999), primary_key=True, nullable=True)
    hours = db.Column(db.String(999), nullable=True)

# бновленные базы