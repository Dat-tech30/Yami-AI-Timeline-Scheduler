from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# Replace with your actual API key path
api_key_path = "path/to/your/api_key.txt"

def load_api_key():
  with open(api_key_path, "r") as f:
    return f.read().strip()

def configure_genai():
  api_key = load_api_key()
  genai.configure(api_key=api_key)

# Configure generation settings
generation_config = {
  "temperature": 0.7,  # Adjust for desired level of creativity
  "top_p": 0.9,        # Focus on more likely words
  "top_k": 20,         # Consider top 20 most likely words
  "max_output_tokens": 256,  # Limit response length
  "response_mime_type": "text/plain",
}

def create_model():
  configure_genai()
  model = genai.GenerativeModel(
      model_name="gemini-1.5-pro",
      generation_config=generation_config,
      system_instruction="Your Advanced Meeting Itinerary",
  )
  return model

model = None  # Initialize model outside a route for global access

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
  global model
  if model is None:
    model = create_model()

  user_input = request.json["message"]
  response = model.send_message(user_input).text
  return jsonify({"response": response})

if __name__ == "__main__":
  app.run(debug=True)