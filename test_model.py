from openai import OpenAI
import os
from app.utils.FunctionCall.openiai_tools import get_function_call_json

GPT_MODEL = "gpt-3.5-turbo-1106"
client = OpenAI(api_key=os.getenv('API_KEY'))
tools = get_function_call_json()

# Step #1: Prompt with content that may result in function call. In this case the model can identify the information requested by the user is potentially available in the database schema passed to the model in Tools description. 
messages = [{
    "role":"user", 
    "content": "Can you generate me a manual test?"
}]

response = client.chat.completions.create(
    model=GPT_MODEL, 
    messages=messages, 
    tools= tools, 
    tool_choice="auto"
)

# Append the message to messages list
response_message = response.choices[0].message 
messages.append(response_message)

print(response_message)

# Step 2: determine if the response from the model includes a tool call.   
tool_calls = response_message.tool_calls
if tool_calls:
    # If true the model will return the name of the tool / function to call and the argument(s)  
    tool_call_id = tool_calls[0].id
    tool_function_name = tool_calls[0].function.name
    tool_query_string = eval(tool_calls[0].function.arguments)['node']
    
    # Step 3: Call the function and retrieve results. Append the results to the messages list.      
    if tool_function_name == 'gen_manual_test':
        
        messages.append({
            "role":"tool", 
            "tool_call_id":tool_call_id, 
            "name": tool_function_name, 
            "content": response_message.tool_calls[0].function.arguments
        })
        
        # Step 4: Invoke the chat completions API with the function response appended to the messages list
        # Note that messages with role 'tool' must be a response to a preceding message with 'tool_calls'
        model_response_with_function_call = client.chat.completions.create(
            model= GPT_MODEL,
            messages=messages,
        )  # get a new response from the model where it can see the function response
        print(model_response_with_function_call.choices[0].message.content)
    else: 
        print(f"Error: function {tool_function_name} does not exist")
else: 
    # Model did not identify a function to call, result can be returned to the user 
    print(response_message.content) 