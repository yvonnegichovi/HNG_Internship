#!/usr/bin/python3
"""
This module creates a basic web server using Flask
"""

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_location_from_ip(ip):
    locationiq_api_key = 'pk.54aee61604854ee6aa9afda8dc076cbf'
    response = requests.get(f'https://us1.locationiq.com/v1/reverse.php?key={locationiq_api_key}&lat=LATITUDE&lon=LONGITUDE&format=json')
    data = response.json()
    if data:
        city = data[0].get('display_name', '').split(',')[0]
        return city
    return None

def get_temperature(city):
    api_key = '169d8032d56c4d0b937213455240207'
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}')
    return response.json().get('current', {}).get('temp_c')

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
