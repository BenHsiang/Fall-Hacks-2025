from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins by default

@app.route('/', methods=['POST', 'OPTIONS'])
def receive_json():
    if request.method == 'OPTIONS':
        # ✅ CORS preflight needs a 200 or 204 response with no body
        return '', 204

    
    if request.is_json:
        data = request.get_json()
        print("Received data:", data)
    
    # Not important, just error messages 
        return jsonify({"message": "Data received successfully!", "received_data": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)