from flask import Blueprint, request, jsonify, render_template, session
import requests
from models import db, User

main_blueprint = Blueprint('main', __name__, url_prefix='/main')

def query_gpt_turbo_chat(question, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a knowledgeable nutritionist and fitness advisor.You want to help people achieve their fitness and health goals. Do not answer any questions that are not food, exercise, nutritional, workout related."},
                     {"role": "user", "content": question}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error in API request: {response.status_code} - {response.text}")

@main_blueprint.route('/')
def home():
    return render_template('chat.html')  

@main_blueprint.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
     #Where chatbot API key would be
    try:
        result = query_gpt_turbo_chat(question, api_key)
        return jsonify(result['choices'][0]['message']['content'])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
