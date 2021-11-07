from flask import Flask, url_for
from datetime import datetime, timedelta
import requests, datetime


app = Flask(__name__)

@app.route('/wheater')
def get_weather():
    params = {"access_key": "YOUR_KEY_FROM_WEATHERSTACK", "query": "Moscow"}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return f"Сейчас в Москве {api_response['current']['temperature']} градусов"

@app.route('/time')
def sabe():
    dtmn = datetime.datetime.now()
    return str(dtmn)


if __name__ == '__main__':
    app.run()
