from app import db
import uuid
from datetime import datetime

class User(db.Model):
    __bind_key__ = 'chat'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sessions = db.relationship('Session', backref='user', lazy=True)

class Session(db.Model):
    __bind_key__ = 'chat'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    messages = db.relationship('ChatMessage', backref='session', lazy=True)

class ChatMessage(db.Model):
    __bind_key__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(36), db.ForeignKey('session.id'), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    content = db.Column(db.Text, nullable=False)

class chat_message(db.Model):
    __bind_key__ = 'flowise'
    id = db.Column(db.String, primary_key=True)
    role = db.Column(db.String, nullable=False)
    chatflowid = db.Column(db.String(36), nullable=False)
    content = db.Column(db.Text, nullable=False)
    createdDate = db.Column(db.DateTime, nullable=False)
    chatType = db.Column(db.String(4), nullable=False)
    chatId = db.Column(db.String(36), nullable=False)

class chat_flow(db.Model):
    __bind_key__ = 'flowise'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flowData = db.Column(db.Text, nullable=False)
    createdDate = db.Column(db.DateTime, nullable=False)
    updatedDate = db.Column(db.DateTime, nullable=False)