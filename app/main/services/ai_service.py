from openai import OpenAI
from app import db
from app.main.models import chat_message, chat_flow
from app.utils.helpers import extract_json_objects, convert, convertWorkflow
import json
import os

client = OpenAI(api_key=os.getenv('API_KEY'))

def generate_text(data):
    session_id = data.get('session_id')
    prompt = data.get('prompt', '')

    context = chat_flow.query.filter_by(id=session_id).first().flowData
    context_file = '/home/adam_skandrani/tpm_back/tmp/context.json'
    with open(context_file, 'w') as file:
        file.write(context)

    convertWorkflow()

    new_context_file = '/home/adam_skandrani/tpm_back/tmp/new_context.json'
    with open(new_context_file, 'r') as f:
        new_context = f.read().replace('\n', '')

    context_prompt = f"{prompt}. Context:{new_context}"

    messages = [{"role": "user" if message.role == "userMessage" else "assistant", "content": message.content} 
                for message in chat_message.query.filter_by(chatflowid=session_id).all()]
    
    system_instruction = "You are a QA engineer responsible for extracting relevant information from user prompts and mapping it to a specific node structure in JSON format..."  # Add the full instruction here

    if not any(message['role'] == 'system' for message in messages):
        messages.insert(0, {"role": "system", "content": system_instruction})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        max_tokens=2048
    )

    assistant_message_content = response.choices[0].message.content.strip()

    json_response = extract_json_objects(assistant_message_content)
    response_file = '/home/adam_skandrani/tpm_back/tmp/json_response.json' 
    with open(response_file, 'w') as file:
        json.dump(json_response, file)

    convert()

    with open('/home/adam_skandrani/tpm_back/tmp/context.json', 'r') as f:
        context_file = json.load(f)

    with open('/home/adam_skandrani/tpm_back/tmp/final_structure.json', 'r') as f:
        json_data_file = json.load(f)

    json_data_string = json.dumps(json_data_file).replace('\n', '')

    return json_data_string, assistant_message_content