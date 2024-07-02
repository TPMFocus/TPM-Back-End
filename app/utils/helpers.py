import json
import logging
from app.main.models import chat_flow
from app.utils.ConvertScript.ConvertScript import convert as Model2Workflow
from app.utils.ConvertScript.Workflow2Model import convertWorkflow as Workflow2Model

wsl_base_path = '/home/adam_skandrani/TPM-Flask-Backend/'
base_path = 'C:/Users/Adam Skandrani/TPM-Flask-Backend'



def extract_json_objects(text):
  """
  Extracts JSON objects from text using the json module.

  Args:
    text (str): The text from which JSON objects will be extracted.

  Returns:
    list: A list of extracted JSON objects.

  """
  decoder = json.JSONDecoder()
  extracted_objects = []
  pos = 0
  while True:
    match = text.find('{', pos)
    if match == -1:
      break
    try:
      obj, end_pos = decoder.raw_decode(text[match:])
      extracted_objects.append(obj)
      pos = end_pos + match
    except json.JSONDecodeError:
      pos += 1  # Skip invalid JSON section
  return extracted_objects



def update_context(data):
  """
  Updates the context for a given session ID.

  Args:
    data (dict): A dictionary containing the session ID.

  Returns:
    str: The updated context.

  Raises:
    dict: An error dictionary with the corresponding error message and status code.

  """
  session_id = data.get('session_id')
  # Fetch context from database
  chat_flow_entry = chat_flow.query.filter_by(id=session_id).first()
  if not chat_flow_entry:
    logging.error(f"No chat flow found for session_id: {session_id}")
    return {"error": "Invalid session_id"}, 400
  context = chat_flow_entry.flowData
  # Write context to file
  context_file = f'{wsl_base_path}/instance/tmp/context.json'
  try:
    with open(context_file, 'w') as file:
      file.write(context)
  except Exception as e:
    logging.error(f"Failed to write context to file: {e}")
    return {"error": "Failed to process context"}, 500
  # Convert workflow
  try:
    convertWorkflow()
  except Exception as e:
    logging.error(f"Failed to convert workflow: {e}")
    return {"error": "Failed to convert workflow"}, 500
  # Read new context
  new_context_file = f'{wsl_base_path}/instance/tmp/new_context.json'
  try:
    with open(new_context_file, 'r') as f:
      new_context = f.read().replace('\n', '')
  except Exception as e:
    logging.error(f"Failed to read new context file: {e}")
    return {"error": "Failed to read new context"}, 500
  return new_context


def concat_elements(dict_input, list_input):
    """
    Concatenates elements from the 'nodes' key in the input dictionary with the given list.
    
    Args:
        dict_input (dict): The input dictionary.
        list_input (list): The list to concatenate with.
    
    Returns:
        list: The concatenated list.
    
    Raises:
        TypeError: If input types are not as expected.
    """
    if not isinstance(dict_input, dict):
        raise TypeError("dict_input must be a dictionary.")
    if not isinstance(list_input, list):
        raise TypeError("list_input must be a list.")
    
    # Extract elements from the 'nodes' key in the input dictionary
    if len(list_input) == 1 and isinstance(list_input[0], dict) and 'nodes' in list_input[0]:
        list_input = list_input[0]['nodes']
    
    nodes = dict_input.get("nodes", [])
    if not isinstance(nodes, list):
        raise TypeError("The 'nodes' key in dict_input must be a list.")
    
    if not nodes:
        return list_input

    # Create a set of node_ids from the list_input for quick lookup
    existing_ids = set()
    for item in list_input:
        if isinstance(item, dict) and "node_id" in item:
            existing_ids.add(item["node_id"])
        else:
            raise TypeError("Each item in list_input must be a dictionary with a 'node_id' key.")
    
    # Iterate through the nodes and add only unique elements based on 'node_id'
    for node in nodes:
        if isinstance(node, dict) and "node_id" in node:
            if node["node_id"] not in existing_ids:
                list_input.append(node)
                existing_ids.add(node["node_id"])
        else:
            raise TypeError("Each node in dict_input['nodes'] must be a dictionary with a 'node_id' key.")
    
    return list_input


def convert():
  Model2Workflow()

def convertWorkflow():
  Workflow2Model()