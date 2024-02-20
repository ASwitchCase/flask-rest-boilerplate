from flask import Blueprint, jsonify, request
from app.services.user_service import *
from app.models.user import User
from ..extentions import db

users = Blueprint("user",__name__,url_prefix="/api/v1/users")

@users.post('/')
def create():
    return jsonify(create_user().to_json())

@users.get('/')
def get_all():
    return jsonify([user.to_json() for user in get_all_users()])

@users.get("/<id>")
def get(id):
    return jsonify(get_user(id).to_json())

@users.put("/<id>")
def update(id):
    return jsonify(update_user(id).to_json())

@users.delete("/<id>")
def delete(id):
    return delete_user(id)
