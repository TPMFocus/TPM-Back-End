from openai import OpenAI
from app import db
from app.main.models import chat_message, chat_flow
from app.utils.helpers import extract_json_objects, convert, convertWorkflow, update_context, concat_elements
from app.utils.FunctionCall.openiai_tools import get_function_call_json
from tenacity import retry, wait_random_exponential, stop_after_attempt
import json
import os
import logging

# wsl_base_path : /home/adam_skandrani/TPM-Flask-Backend/
base_path = 'C:/Users/Adam Skandrani/TPM-Flask-Backend'

GPT_MODEL = "gpt-3.5-turbo-1106"
client = OpenAI(api_key=os.getenv('API_KEY'))

def generate_text(data):
    try:
        session_id = data.get('session_id')
        prompt = data.get('prompt', '')

        new_context = update_context(data)

        context_prompt = f"{prompt}. Here's what we currently have in the workflow:{new_context}"

        # Fetch messages from database, including the latest prompt as a message
        try:
            messages = [{"role": "user" if message.role == "userMessage" else "assistant", "content": message.content} 
                        for message in chat_message.query.filter_by(chatflowid=session_id).all()]
            # Add the latest prompt as a new user message
            messages.append({"role": "user", "content": context_prompt})
        except Exception as e:
            logging.error(f"Failed to fetch chat messages: {e}")
            return {"error": "Failed to fetch messages"}, 500

        # Ensure system instruction is included
        system_instruction= "You are a QA engineer responsible for extracting relevant information from user prompts and mapping it to a specific node structure in JSON format. Follow the guidelines below for creating the JSON nodes:\n\n1/ Node Definitions: Each node has specific attributes and follows a unique structure. Ensure all required fields are correctly populated.\n\n2/ Child Nodes: Certain nodes can have child nodes. Ensure correct parent-child relationships:\n-Test steps are child nodes of Manual Test Cases. They're used to provide more details to the manual tests.\n-UI interactions are child nodes of Automated Test Cases. They're used to provide more details to the automated tests.\n-Frontend and Backend Unit Test Nodes are child nodes of Unit Test Node.\n-Frontend and Backend Integration Nodes are child nodes of Integration Test Node.\n\n3/ General Workflow:\n-Test Strategy: The starting point.\n-Test Phases: Multiple phases can follow a test strategy.\n-Test Plans: Multiple plans can follow a test phase.\n-Test Suites: Multiple suites can follow a test plan.\n-Test Cases: (Unit, Integration, Performance, Security, Code Quality, Third Party) can follow a test suite.\n-Detailed Test Cases: (Manual, Automated, BDD) can follow test cases with optional detailed steps or UI interactions.\n\n4/ Output Format: Each node should be a separate JSON object. The next_node attribute contains references to subsequent nodes by their node_id.\n\n5/ Node Structure:\n```json{\n  \"node\": \"NodeType\",\n  \"node_id\": \"\",\n  \"data\": {\n    // Specific attributes for the node type\n  },\n  \"next_node\": []\n}```\n\n6/ Node Types and Attributes:\n-TestStrategyNode:\n```json{\n  \"node\": \"TestStrategyNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"dataConsiderations\": \"\"\n  },\n  \"next_node\": []\n}```\n-TestingPhaseNode:\n```json{\n  \"node\": \"TestingPhaseNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"startDate\": \"\",\n    \"endDate\": \"\",\n    \"estimation\": \"\"\n  },\n  \"next_node\": []\n}```\n-TestPlanNode:\n```json{\n  \"node\": \"TestPlanNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"numberOfAssignedTesters\": \"\",\n    \"dateOfExecution\": \"\",\n    \"estimation\": \"\",\n    \"riskAssessment\": \"\",\n    \"dataRequirements\": \"\",\n    \"overallExecutionResults\": \"\"\n  },\n  \"next_node\": []\n}```\n-TestSuiteNode:\n```json{\n  \"node\": \"TestSuiteNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"exitCriteria\": \"\"\n  },\n  \"next_node\": []\n}```\n-ManualTestCaseNode:\n```json{\n  \"node\": \"ManualTestCaseNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"preconditions\": \"\",\n    \"postconditions\": \"\",\n    \"expectedResults\": \"\",\n    \"actualResults\": \"\",\n    \"testData\": \"\",\n    \"assignedTesters\": \"\"\n  },\n  \"next_node\": []\n}```\n-TestStepNode:\n```json{\n  \"node\": \"TestStepNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"stepId\": \"\",\n    \"description\": \"\",\n    \"requiredInput\": \"\",\n    \"expectedOutput\": \"\"\n  },\n  \"next_node\": []\n}```\n-AutomatedTestCaseNode:\n```json{\n  \"node\": \"AutomatedTestCaseNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"preconditions\": \"\",\n    \"postconditions\": \"\",\n    \"expectedResults\": \"\",\n    \"actualResults\": \"\",\n    \"scriptLocation\": \"\",\n    \"programmingLanguage\": \"\",\n    \"framework\": \"\",\n    \"maintenanceEffort\": \"\",\n    \"dependencies\": \"\"\n  },\n  \"next_node\": []\n}```\n-UIInteractionNode:\n```json{\n  \"node\": \"UIInteractionNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"elementType\": \"\",\n    \"identifier\": \"\",\n    \"action\": \"\",\n    \"value\": \"\"\n  },\n  \"next_node\": []\n}```\n-BDDTestCaseNode:\n```json{\n  \"node\": \"BDDTestCaseNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"background\": \"\",\n    \"scenario\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"gherkinSteps\": [\n      { \"keyword\": \"Given\", \"text\": \"\" },\n      { \"keyword\": \"When\", \"text\": \"\" },\n      { \"keyword\": \"Then\", \"text\": \"\" }\n    ]\n  },\n  \"next_node\": []\n}```\n-UnitTestNode:\n```json{\n  \"node\": \"UnitTestNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"targetLayer\": \"Front-End\" / \"Back-End\"\n  },\n  \"next_node\": []\n}```\n-FrontEndUnitTestNode:\n```json{\n  \"node\": \"FrontEndUnitTestNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"UITestFramework\": \"\",\n    \"UIElements\": \"\"\n  },\n  \"next_node\": []\n}```\n-BackendUnitTestNode:\n```json{\n  \"node\": \"BackendUnitTestNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"UnitTestClass\": \"\",\n    \"Mocking\": \"\"\n  },\n  \"next_node\": []\n}```\n-IntegrationTestNode:\n```json{\n  \"node\": \"IntegrationTestNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"targetLayer\": \"Front-End\" / \"Back-End\"\n  },\n  \"next_node\": []\n}```\n-FrontendIntegrationNode:\n```json{\n  \"node\": \"FrontendIntegrationNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"IntegrationScope\": \"\",\n    \"FrontEndTechnology\": \"\"\n  },\n  \"next_node\": []\n}```\n-BackendIntegrationNode:\n```json{\n  \"node\": \"BackendIntegrationNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"IntegrationScope\": \"\",\n    \"BackendTechnology\": \"\"\n  },\n  \"next_node\": []\n}```\n-PerformanceTestNode:\n```json{\n  \"node\": \"PerformanceTestNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"metrics\": {\n      \"responseTime\": \"\",\n      \"throughput\": \"\",\n      \"resourceUtilization\": \"\"\n    },\n    \"tools\": \"\"\n  },\n  \"next_node\": []\n}```\n-SecurityTestNode:\n```json{\n  \"node\": \"SecurityTestNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"tools\": \"\",\n    \"type\": \"Penetration Testing\" / \"Vulnerability Scanning\" / \"Other\"\n  },\n  \"next_node\": []\n}```\n-CodeQualityChecksNode:\n```json{\n  \"node\": \"CodeQualityChecksNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"checks\": {\n      \"Code Coverage\": \"\",\n      \"Static Code Analysis\": \"\"\n    },\n    \"tools\": \"\"\n  },\n  \"next_node\": []\n}```\n-ThirdPartyChecksNode:\n```json{\n  \"node\": \"ThirdPartyChecksNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"title\": \"\",\n    \"description\": \"\",\n    \"priority\": \"\",\n    \"tags\": \"\",\n    \"type\": \"\",\n    \"tools\": \"\"\n  },\n  \"next_node\": []\n}```\n-TestEnvironmentNode:\n```json{\n  \"node\": \"TestEnvironmentNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"name\": \"\",\n    \"URL\": \"\",\n    \"database\": \"\",\n    \"credentials\": \"\",\n    \"tools\": \"\"\n  },\n  \"next_node\": []\n}```\n-IntegrationNode:\n```json{\n  \"node\": \"IntegrationNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"JIRA_URL\": \"\",\n    \"projectKey\": \"\",\n    \"authentication\": \"\"\n  },\n  \"next_node\": []\n}```\n-NoteNode:\n```json{\n  \"node\": \"NoteNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"content\": \"\"\n  },\n  \"next_node\": []\n}```\n-ExecutionDetailsNode:\n```json{\n  \"node\": \"ExecutionDetailsNode\",\n  \"node_id\": \"\",\n  \"data\": {\n    \"dateOfExecution\": \"\",\n    \"estimation\": \"\",\n    \"realExecutionTime\": \"\",\n    \"passFailStatus\": \"\"\n  },\n  \"next_node\": []\n}```\n\n7/ Node Relationships:\n-Ensure nodes are linked properly using the next_node attribute, containing the node_id of the subsequent node.\n-A test strategy can have multiple test phases, a test phase can have multiple test plans, and so on.\n\n8/ Partial Workflows: If the user's prompt is not detailed enough to create a fully detailed workflow, create the nodes based on the provided details.\nExample of a Partial Workflow:\n```json{\n  \"node\": \"TestStrategyNode\",\n  \"node_id\": \"1\",\n  \"data\": {\n    \"title\": \"Initial Strategy\",\n    \"description\": \"Defining the overall strategy\",\n    \"dataConsiderations\": \"Consider GDPR regulations\"\n  },\n  \"next_node\": [\"2\"]\n},\n{\n  \"node\": \"TestingPhaseNode\",\n  \"node_id\": \"2\",\n  \"data\": {\n    \"title\": \"Phase 1\",\n    \"description\": \"Initial testing phase\",\n    \"startDate\": \"2023-01-01\",\n    \"endDate\": \"2023-02-01\",\n    \"estimation\": \"1 month\"\n  },\n  \"next_node\": []\n}```"
        if not any(message['role'] == 'system' for message in messages):
            messages.insert(0, {"role": "system", "content": system_instruction})

        # Generate response using OpenAI API
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                messages=messages,
                max_tokens=4096
            )
        except Exception as e:
            logging.error(f"OpenAI API call failed: {e}")
            return {"error": "Failed to generate response"}, 500

        assistant_message_content = response.choices[0].message.content.strip()

        try:
            json_response = extract_json_objects(assistant_message_content)
            # Add context to response
            try:
                json_response = concat_elements(json.loads(new_context), json_response)
            except Exception as e:
                logging.error(f"Failed to concatenate context and response: {e}")
                return {"error": "Failed to process response"}, 500 
            
            response_file = f'{base_path}/instance/tmp/json_response.json'
            with open(response_file, 'w') as file:
                json.dump(json_response, file)
        except Exception as e:
            logging.error(f"Failed to extract or save JSON response: {e}")
            return {"error": "Failed to process response"}, 500

        # Convert response
        try:
            convert()
        except Exception as e:
            logging.error(f"Failed to convert response: {e}")
            return {"error": "Failed to convert response"}, 500

        # Load final context and structure
        try:
            with open(f'{base_path}/instance/tmp/context.json', 'r') as f:
                context_file = json.load(f)
            with open(f'{base_path}/instance/tmp/final_structure.json', 'r') as f:
                json_data_file = json.load(f)
        except Exception as e:
            logging.error(f"Failed to load final context or structure: {e}")
            return {"error": "Failed to load final data"}, 500

        json_data_string = json.dumps(json_data_file).replace('\n', '')

        return json_data_string, assistant_message_content
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred"}, 500
    

def generate_func_call(data):
    try:
        session_id = data.get('session_id')
        prompt = data.get('prompt', '')

        new_context = update_context(data)

        context_prompt = f"{prompt}. Context:{new_context}"

        # Fetch messages from database, including the latest prompt as a message
        try:
            messages = [{"role": "user" if message.role == "userMessage" else "assistant", "content": message.content} 
                        for message in chat_message.query.filter_by(chatflowid=session_id).all()]
            # Add the latest prompt as a new user message
            messages.append({"role": "user", "content": context_prompt})
        except Exception as e:
            logging.error(f"Failed to fetch chat messages: {e}")
            return {"error": "Failed to fetch messages"}, 500

        # Ensure system instruction is included
        system_instruction = "You are a QA engineer responsible for extracting relevant information from user prompt and mapping each element detected to its corresponding JSON format. Always fill the node type. Do not forget to fill the node_id and next_node fields. The next_node field should contain the node_id of the next node in the workflow. If the user prompt is not detailed enough to create a fully detailed workflow, create the nodes based on the provided details."
        if not any(message['role'] == 'system' for message in messages):
            messages.insert(0, {"role": "system", "content": system_instruction})

        @retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
        def chat_completion_request(messages, tools=None, tool_choice="auto", model=GPT_MODEL):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    tools=tools,
                    tool_choice=tool_choice,
                    max_tokens=4096
                )
                return response
            except Exception as e:
                print("Unable to generate ChatCompletion response")
                print(f"Exception: {e}")
                return e
        
        tools = get_function_call_json()

        chat_response = chat_completion_request(messages, tools=tools, model=GPT_MODEL)

        assistant_message = chat_response.choices[0].message.tool_calls
        assistant_message_content = []
        # Extract the arguments dictionary
        for i in range(len(assistant_message)):
            assistant_message_content.append(assistant_message[i].function.arguments)

        assistant_message_content = str(assistant_message_content)
        # Extract and save JSON response
        try:
            json_response = extract_json_objects(assistant_message_content)
            # Add context to response
            json_response = concat_elements(json.loads(new_context), json_response)

            response_file = f'{base_path}/instance/tmp/json_response.json'
            with open(response_file, 'w') as file:
                json.dump(json_response, file)
        except Exception as e:
            logging.error(f"Failed to extract or save JSON response: {e}")
            return {"error": "Failed to process response"}, 500
        
        # Convert response
        try:
            convert()
        except Exception as e:
            logging.error(f"Failed to convert response: {e}")
            return {"error": "Failed to convert response"}, 500

        # Load final context and structure
        try:
            with open(f'{base_path}/instance/tmp/context.json', 'r') as f:
                context_file = json.load(f)
            with open(f'{base_path}/instance/tmp/final_structure.json', 'r') as f:
                json_data_file = json.load(f)
        except Exception as e:
            logging.error(f"Failed to load final context or structure: {e}")
            return {"error": "Failed to load final data"}, 500
        
        json_data_string = json.dumps(json_data_file).replace('\n', '')

        return json_data_string, assistant_message_content

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred"}, 500
        