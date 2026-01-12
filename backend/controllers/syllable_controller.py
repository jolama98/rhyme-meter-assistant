from flask import jsonify, request
from models.syllable_counter import SyllableCounter

# Initialize syllable counter once (reused for all requests)
syllable_counter = SyllableCounter()

def count_syllables():
    """API endpoint to count syllables"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({
                'syllables': [],
                'total': 0
            })
        
        # Count syllables using our model
        results = syllable_counter.count_text_syllables(text)
        
        # Calculate total
        total = sum(line['syllables'] for line in results)
        
        return jsonify({
            'syllables': results,
            'total': total
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'syllables': [],
            'total': 0
        }), 500