import json
from app.utils.ConvertScript.ConvertScript import convert as Model2Workflow
from app.utils.ConvertScript.Workflow2Model import convertWorkflow as Workflow2Model


def extract_json_objects(text):
  """
  Extracts JSON objects from text using the json module.
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

def convert():
    Model2Workflow()

def convertWorkflow():
    Workflow2Model()