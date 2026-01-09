from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Load configuration
app.config['DATABASE'] = 'database.db'
app.config['DATA_DIR'] = os.path.join(os.path.dirname(__file__), 'data')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Rhyme & Meter Assistant API"})

@app.route('/api/syllables', methods=['POST'])
def count_syllables():
    data = request.get_json()
    text = data.get('text', '')
    # TODO: Implement syllable counting
    return jsonify({"syllables": [], "total": 0})

@app.route('/api/rhymes', methods=['POST'])
def find_rhymes():
    data = request.get_json()
    word = data.get('word', '')
    # TODO: Implement rhyme finding
    return jsonify({"rhymes": []})

@app.route('/api/scheme', methods=['POST'])
def detect_scheme():
    data = request.get_json()
    text = data.get('text', '')
    # TODO: Implement scheme detection
    return jsonify({"scheme": ""})

@app.route('/api/forms', methods=['GET'])
def get_forms():
    import json
    forms_path = os.path.join(app.config['DATA_DIR'], 'forms.json')
    with open(forms_path, 'r') as f:
        forms_data = json.load(f)
    return jsonify(forms_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
