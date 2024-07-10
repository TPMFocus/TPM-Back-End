import re
import json

class JSONUtils:
    json_pattern = re.compile(r'\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\}')

    @staticmethod
    def is_json(candidate: str) -> bool:
        try:
            json.loads(candidate)
            return True
        except ValueError:
            return False

    @staticmethod
    def find_and_remove_json_objects(text: str) -> str:
        while True:
            matches = JSONUtils.json_pattern.findall(text)
            if not matches:
                break
            for match in matches:
                if JSONUtils.is_json(match):
                    text = text.replace(match, '')
        return text
    
    @staticmethod
    def extract_json_objects(text: str) -> list:
        extracted_objects = []
        pos = 0
        while True:
            match = text.find('{', pos)
            if match == -1:
                break
            try:
                obj, end_pos = json.JSONDecoder().raw_decode(text[match:])
                extracted_objects.append(obj)
                pos = end_pos + match
            except json.JSONDecodeError:
                pos += 1
        return extracted_objects

    @staticmethod
    def combine_json(json1: dict, json2: dict) -> dict:
        return {
            "nodes": json1.get("nodes", []) + json2.get("nodes", []),
            "edges": json1.get("edges", []) + json2.get("edges", [])
        }