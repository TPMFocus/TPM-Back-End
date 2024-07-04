from app.utils.ConvertScript.Structure import *
from app.utils.ConvertScript.Extract import *
from app.utils.ConvertScript.Build import *
import json

wsl_base_path = '/home/adam_skandrani/TPM-Flask-Backend/'
base_path = 'C:/Users/Adam Skandrani/TPM-Flask-Backend'

def convert():
    # Extracting data from the json file
    try:
        json_data_list = extract_json_data()  # Assuming this function returns the JSON string
    except Exception as e:
        print('Error extracting JSON data : ', e)
        return
    
    try:
        parsed_data = json.loads(json_data_list)  # Correctly parsing the JSON string
        #print('Extracted data : ', parsed_data)
    except Exception as e:
        print('Error parsing JSON data : ', e)
        return
    
    try:
        if isinstance(parsed_data, list) and len(parsed_data) > 0 and isinstance(parsed_data[0], dict) and "nodes" in parsed_data[0]:
            nodes_data = parsed_data[0]["nodes"]  # Extracting nodes data from the parsed JSON
        else:
            nodes_data = parsed_data
    except Exception as e:
        print('Error extracting nodes data : ', e)
        return
        
    #print('Nodes data : ', nodes_data)
    
    # Creating the structure
    try:
        final_structure_node, final_structure_edge = build(nodes_data)
    except Exception as e:
        print('Error building structure : ', e)
        return
    
    # Saving final_structure to a JSON file
    try:
        with open(f'{wsl_base_path}/instance/tmp/final_structure.json', 'w') as file:
            json.dump({"nodes": final_structure_node, "edges": final_structure_edge}, file, indent=2)
    except Exception as e:
        print('Error saving final structure : ', e)
        return