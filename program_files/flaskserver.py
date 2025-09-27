from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.json
    else:
        data = request.form

    print("Received data:", data)
    return jsonify({"status": "success"})  # Return valid JSON

if __name__ == '__main__': app.run(debug=True) # This keeps the app running