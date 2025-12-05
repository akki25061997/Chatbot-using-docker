from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow browser access

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()

    if "hello" in user_message:
        reply = "Hi! How can I help you?"
    elif "hi" in user_message:
        reply = "Hello! I am your chatbot."
    elif "how are you" in user_message:
        reply = "I am fine! Thanks for asking 😊"
    else:
        reply = "I am a simple chatbot. Try saying: hello 👋"

    return jsonify({"response": reply})

@app.route('/')
def home():
    return jsonify({"message": "Chatbot API is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
