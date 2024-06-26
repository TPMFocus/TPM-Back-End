from app import db
from app.main.models import User, Session, ChatMessage, chat_message, chat_flow
from datetime import datetime
import uuid

def create_or_update_session(data):
    user_id = data.get('user_id')
    session_id = data.get('session_id')

    user = User.query.filter_by(id=user_id).first()
    if user is None:
        user = User(id=user_id)
        db.session.add(user)

    session = Session.query.filter_by(id=session_id).first()
    if session is None:
        session = Session(id=session_id, user_id=user.id)
        db.session.add(session)
    else:
        session.user_id = user.id

    db.session.commit()
    return {"session_id": session_id}

def add_message(session_id, role, content, chatflowid=None):
    user_message = ChatMessage(session_id=session_id, role=role, content=content)
    db.session.add(user_message)

    if chatflowid:
        flowise_message = chat_message(
            id=str(uuid.uuid4()),
            role=role,
            chatflowid=chatflowid,
            content=content,
            createdDate=datetime.now(),
            chatType='INTERNAL',
            chatId=str(uuid.uuid4())
        )
        

    db.session.commit()
    return flowise_message if chatflowid else user_message

def clear_chat(session_id):
    ChatMessage.query.filter_by(session_id=session_id).delete()
    chat_message.query.filter_by(chatflowid=session_id).delete()
    db.session.commit()

def clear_user_sessions(user_id):
    User.query.filter_by(id=user_id).delete()
    Session.query.filter_by(user_id=user_id).delete()
    db.session.commit()

def update_chat_flow(session_id, flow_data):
    chat_flow.query.filter_by(id=session_id).update(dict(flowData=flow_data))
    db.session.commit()