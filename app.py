

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Your OpenAI API key
API_KEY = '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'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    # Make a request to the OpenAI API
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': 'gpt-3.5-turbo',  # Specify the model you want to use
        'messages': [{'role': 'user', 'content': user_input}]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)


    if response.status_code == 200:
        response_data = response.json()
        ai_response = response_data['choices'][0]['message']['content']
        return jsonify({'response': ai_response})
    else:
        error_message = response.json()
        print("Error from API:", error_message)
        return jsonify({'error': 'Error contacting AI model', 'details': error_message}), response.status_code





if __name__ == '__main__':
    app.run(debug=True)