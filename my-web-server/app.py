#!/usr/bin/python3
"""
This module creates a basic web server using Flask
"""

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_location_from_ip(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    return response.json().get('city')

def get_temperature(city):
    api_key = 'YOUR_WEATHER_API_KEY'  # Replace with your actual weather API key
    response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}')
    return response.json().get('current', {}).get('temperature')

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr

    try:
        location = get_location_from_ip(client_ip)
        temperature = get_temperature(location)

        response = {
            "client_ip": client_ip,
            "location": location,
            "greeting": f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {location}"
        }
    except Exception as e:
        response = {"error": str(e)}

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
