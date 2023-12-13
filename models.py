# models.py
from datetime import datetime
from appFactory import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # Establishing a relationship to food logs
    food_logs = db.relationship('FoodLog', backref='user', lazy=True)

class FoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=True)
    protein = db.Column(db.Float, nullable=True)
    fat = db.Column(db.Float, nullable=True)
    carbohydrate = db.Column(db.Float, nullable=True)
    logged_at = db.Column(db.DateTime, default=datetime.utcnow)