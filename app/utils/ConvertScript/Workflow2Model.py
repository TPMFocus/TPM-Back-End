from app.utils.ConvertScript.Destructure import *
import json

def convertWorkflow():
    file_path = '/home/adam_skandrani/TPM-Flask-Backend/instance/tmp/context.json'
    with open(file_path) as f:
        json_data = json.load(f)
    # Extracting data from the json file
    json_node_list = json_data.get("nodes", [])
    json_edge_list = json_data.get("edges", [])
    edge_list = edge_destructure(json_edge_list)
    # Creating the structure
    new_data = destructure(json_node_list, edge_list)
    # Saving final_structure to a JSON file
    with open('/home/adam_skandrani/TPM-Flask-Backend/instance/tmp/new_context.json', 'w') as file:
        json.dump({"nodes": new_data}, file, indent=2)