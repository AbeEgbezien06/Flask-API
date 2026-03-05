#import flask and jsonify to create asimple API that returns the sensitive data in JSON format 
from flask import Flask, jsonify, request
import os

#creating a dictionary filled with sensitive data '\
app = Flask(__name__)
sensitive_data = {
    "username": "onlyonebarry",
    "password": "only_for_barry123",
    "address": "123 Main Street, Anytown, USA",
    "SSN": "24-26-1234"
}
#retrieving the API key from the environment variable and setting a default value if the environment variable is not set
key = os.getenv("API_KEY", "changeme123")

def is_key():
   #checking if the API key provided in the request headers matches the expected key and returning a boolean value accordingly
   return request.headers.get("X-API-Key") == key
    

#creating an endpoint that returns the sensitive data in Json format from the api whem a GET request is made to the sensitive data endpoint 
@app.get('/data')
def data():
    if not is_key():
        return jsonify({"error": "Invalid API key"}), 401
    return jsonify(sensitive_data)


#running tht flask app on the local development server 
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000 )

