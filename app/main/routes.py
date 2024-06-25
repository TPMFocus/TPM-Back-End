from flask import Blueprint, request, jsonify
from app.main.services import ai_service, database_service

bp = Blueprint('main', __name__)

@bp.route('/start-session', methods=['POST'])
def start_session():
    data = request.get_json()
    if not data or 'user_id' not in data:
        return jsonify({"error": "User ID is required"}), 400
    
    result = database_service.create_or_update_session(data)
    return jsonify(result)

@bp.route('/generate-text', methods=['POST'])
def generate_text():
    if request.headers.get('Content-Type') != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    if not data or 'session_id' not in data or 'prompt' not in data:
        return jsonify({"error": "Invalid input"}), 400

    json_data_string, assistant_message_content = ai_service.generate_text(data)
    
    database_service.update_chat_flow(data['session_id'], json_data_string)
    assistant_message = database_service.add_message(data['session_id'], 'assistant', assistant_message_content, data['session_id'])

    return jsonify({
        "generated_text": assistant_message.content,
        "chatId": assistant_message.chatId,
        "createdDate": assistant_message.createdDate
    })

@bp.route('/clear-chat', methods=['POST'])
def clear_chat():
    data = request.get_json()
    if not data or 'session_id' not in data:
        return jsonify({"error": "Session ID is required"}), 400

    database_service.clear_chat(data['session_id'])
    return jsonify({"message": "Chat history has been cleared"})