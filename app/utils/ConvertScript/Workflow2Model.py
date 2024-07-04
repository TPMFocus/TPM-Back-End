from app.utils.ConvertScript.Destructure import *
import json

wsl_base_path = '/home/adam_skandrani/TPM-Flask-Backend'
base_path = 'C:/Users/Adam Skandrani/TPM-Flask-Backend'

def convertWorkflow():
    file_path = f'{wsl_base_path}/instance/tmp/context.json'
    with open(file_path) as f:
        json_data = json.load(f)
    # Extracting data from the json file
    try:
        json_node_list = json_data.get("nodes", [])
        json_edge_list = json_data.get("edges", [])
    except Exception as e:
        print('Error extracting JSON data : ', e)
        return
    
    try:
        edge_list = edge_destructure(json_edge_list)
    except Exception as e:
        print('Error deconstructing edges : ', e)
        return
    try:
        # Creating the structure
        new_data = destructure(json_node_list, edge_list)
    except Exception as e:
        print('Error deconstructing nodes : ', e)
        return
    
    try:
        # Saving final_structure to a JSON file
        with open(f'{wsl_base_path}/instance/tmp/new_context.json', 'w') as file:
            json.dump({"nodes": new_data}, file, indent=2)
    except Exception as e:
        print('Error saving new context : ', e)
        return