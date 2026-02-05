from config import GEMINI_API_KEY
from google import genai
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)
weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}
def get_current_temperature(location):
        # Mock response for demo purposes
        return f"The current temperature in {location} is 68°F."
tools = types.Tool(function_declarations=[weather_function])
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the current temperature in San Francisco?",
    config=types.GenerateContentConfig(tools=[tools]),
)

if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")
    temperature_info = get_current_temperature(**function_call.args)
    print(temperature_info)
else:
    print("No function call found in the response.")
    print(response.text)