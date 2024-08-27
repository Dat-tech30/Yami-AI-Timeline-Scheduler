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


response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)