from flask import Flask, request, jsonify
from flask_cors import CORS
import ClassCart
import ClassDish
import json
# Sets up flask
app = Flask(__name__)
# No idea wtf this does but its very important
CORS(app)

# This function auto-runs when we recieve a POST from the website
@app.route('/', methods=['POST', 'OPTIONS'])
def receive_json():
    # No idea wtf this does but its very important
    if request.method == 'OPTIONS':
        return '', 204

    # The important part, data has the order information
    if request.is_json:
        data = request.get_json()
        print("Received data:", data)
        #moving data from data into cart class
        #assuming calls for data are like this though I wouldnt know. 
        #prays in will run
       # dataloaded=json.loads(data)
       # MyCart=ClassCart.Cart(1111,"User")
        #for x in dataloaded:
        #   Dish=ClassDish.Dish(x.price,0,x.title,x.restaurant)
        #   MyCart.addDishToCart(Dish,1)
        #MyCart.PrintOrder

    
    # Not important, just error messages 
        return jsonify({"message": "Data received successfully!", "received_data": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

# Makes the server run
if __name__ == '__main__':
    app.run(debug=True)