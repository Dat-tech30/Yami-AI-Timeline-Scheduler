"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
"""
For privacy reasons I removed/hidden some parts of the code for the AI, API key, and training for YAMI, however all code here is publicly free from
Google AI Studio and also on this repository for you to see on this commit. Thank you!

"""
import os
import google.generativeai as genai

# This code reads the API key from the file 'api_key.txt' and configures the 'genai' library to utilize with interaction with the AI model
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

genai.configure(api_key="my api key")

# Create the model
generation_config = {
  "temperature": #input_value,
  "top_p": #input_value,
  "top_k": #input_value,
  "max_output_tokens": #input_value,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Your Advanced Meeting Itinerary",
)

chat_session = model.start_chat(
  history=[
   # Chat history is here where I trained the AI model (YAMI)
  ])



# Start a conversation
'''
- Creating an infinite loop with 'While' until it is stopped manually or encounters a error
- Getting user Input from the user to then storing it
- send_message method of the chat_session object passing the input as an argument
- chat_session object handles the interaction with the AI model and continues the loop indefinitely
'''
while True:
    user_input = input("You: ")
    response = chat_session.send_message(user_input)
    print("YAMI:", response.text)
