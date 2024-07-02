from app.utils.ConvertScript.Structure import *
from app.utils.ConvertScript.Extract import *
from app.utils.ConvertScript.Build import *
import json

wsl_base_path = '/home/adam_skandrani/TPM-Flask-Backend/'
base_path = 'C:/Users/Adam Skandrani/TPM-Flask-Backend'

def convert():
    # Extracting data from the json file
    json_data_list = extract_json_data()  # Assuming this function returns the JSON string


    parsed_data = json.loads(json_data_list)  # Correctly parsing the JSON string
    #print('Extracted data : ', parsed_data)
    
    if isinstance(parsed_data, list) and len(parsed_data) > 0 and isinstance(parsed_data[0], dict) and "nodes" in parsed_data[0]:
        nodes_data = parsed_data[0]["nodes"]  # Extracting nodes data from the parsed JSON
    else:
        nodes_data = parsed_data
        
    #print('Nodes data : ', nodes_data)
    
    # Creating the structure
    final_structure_node, final_structure_edge = build(nodes_data)
    
    # Saving final_structure to a JSON file
    with open(f'{wsl_base_path}/instance/tmp/final_structure.json', 'w') as file:
        json.dump({"nodes": final_structure_node, "edges": final_structure_edge}, file, indent=2)