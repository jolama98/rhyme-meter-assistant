from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json

# Import controllers (we'll build these)
from controllers import syllable_controller

app = Flask(__name__)
CORS(app)

# Configuration
app.config['DATABASE'] = 'database.db'
app.config['DATA_DIR'] = os.path.join(os.path.dirname(__file__), 'data')

# ============================================
# HEALTH CHECK
# ============================================
@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if API is running"""
    return jsonify({
        "status": "healthy", 
        "message": "Rhyme & Meter Assistant API"
    })

# ============================================
# SYLLABLE COUNTER
# ============================================
@app.route('/api/syllables', methods=['POST'])
def count_syllables():
    """Count syllables in text - delegates to controller"""
    return syllable_controller.count_syllables()

# ============================================
# RHYME FINDER
# ============================================
@app.route('/api/rhymes', methods=['POST'])
def find_rhymes():
    """Find rhymes for a word"""
    data = request.get_json()
    word = data.get('word', '')
    # TODO: Implement rhyme finding via controller
    return jsonify({"rhymes": []})

# ============================================
# RHYME SCHEME DETECTOR
# ============================================
@app.route('/api/scheme', methods=['POST'])
def detect_scheme():
    """Detect rhyme scheme in poem"""
    data = request.get_json()
    text = data.get('text', '')
    # TODO: Implement scheme detection via controller
    return jsonify({"scheme": ""})

# ============================================
# POETRY FORMS LIBRARY
# ============================================
@app.route('/api/forms', methods=['GET'])
def get_forms():
    """Get all poetry forms"""
    forms_path = os.path.join(app.config['DATA_DIR'], 'forms.json')
    with open(forms_path, 'r') as f:
        forms_data = json.load(f)
    return jsonify(forms_data)

# ============================================
# POEM CRUD (Coming next!)
# ============================================
@app.route('/api/poems', methods=['GET'])
def get_poems():
    """Get all saved poems"""
    # TODO: Implement via poem_controller
    return jsonify({"poems": []})

@app.route('/api/poems', methods=['POST'])
def create_poem():
    """Save a new poem"""
    # TODO: Implement via poem_controller
    return jsonify({"message": "Not implemented yet"})

@app.route('/api/poems/<int:poem_id>', methods=['GET'])
def get_poem(poem_id):
    """Get a specific poem by ID"""
    # TODO: Implement via poem_controller
    return jsonify({"message": "Not implemented yet"})

@app.route('/api/poems/<int:poem_id>', methods=['DELETE'])
def delete_poem(poem_id):
    """Delete a poem"""
    # TODO: Implement via poem_controller
    return jsonify({"message": "Not implemented yet"})

# ============================================
# RUN THE APP
# ============================================
if __name__ == '__main__':
    app.run(debug=True, port=5000)