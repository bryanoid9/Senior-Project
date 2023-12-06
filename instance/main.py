from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

def query_gpt_turbo_chat(question, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a knowledgeable nutritionist and fitness advisor.You want to help people achieve their fitness and health goals."},
                     {"role": "user", "content": question}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error in API request: {response.status_code} - {response.text}")

@app.route('/')
def home():
    return render_template('chat.html')  # Ensure you have an 'index.html' in your 'templates' folder

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    api_key = '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'  #API key
    try:
        result = query_gpt_turbo_chat(question, api_key)
        return jsonify(result['choices'][0]['message']['content'])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
