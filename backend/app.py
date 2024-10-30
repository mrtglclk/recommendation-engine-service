# backend/app.py
from flask import Flask, request, jsonify
from recommendation import get_recommendations
from feedback import save_feedback
from middleware import setup_middleware

app = Flask(__name__)
setup_middleware(app)  # Adds shared middleware for logging, error handling, etc.

# Endpoint for getting recommendations
@app.route('/recommendations', methods=['GET'])
def recommendations():
    user_id = request.args.get('user_id')
    recommendations = get_recommendations(user_id)
    return jsonify({"status": "success", "data": recommendations})

# Endpoint for saving feedback
@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_data = request.json
    save_feedback(feedback_data)
    return jsonify({"status": "success", "message": "Feedback saved"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
