from datetime import datetime
from ..extentions import db
import uuid

class User(db.Model):
    id = db.Column(db.String,primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())
    
    def __repr__(self) -> str:
        return f'User>>> {self.username}'
    
    def to_json(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'password' : self.password,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at,

        }