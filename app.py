from flask import Flask, request, jsonify, render_template
from dialogflow_client import detect_intent_texts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')
    user_text = query_result.get('queryText')
    response_text = detect_intent_texts('suh-3-429200', 'unique-session-id', [user_text], 'ko')
    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
