from flask import Blueprint, jsonify, request
from app.models.user import User
from ..extentions import db

def create_user():
    user = User(
        username=request.json.get('username'),
        email=request.json.get('email'),
        password=request.json.get('password')
    )
    db.session.add(user)
    db.session.commit()

    return user

def get_user(id):
    user = User.query.get(id)
    return user

def get_all_users():
    users = User.query.all()
    return users

def update_user(id):
    user = User.query.get(id)
    user.username = request.json.get('username',user.username)
    user.email = request.json.get('email',user.email)
    user.password = request.json.get('password',user.password)
    db.session.commit()
    return user

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "User deleted"