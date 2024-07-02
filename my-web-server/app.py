#!/usr/bin/python3
"""
This module creates a basic web server using Flask
"""

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr

    location = "New York"
    temperature = 11
    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {location}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
