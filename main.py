import json
import requests
from flask import Flask, request, render_template

API_KEY = "9f324341e4388ec28f907517b769a265"

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict_weather', methods=['GET', 'POST'])
def predict_weather():
    if request.method == 'POST':
        location = request.form['location']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={'9f324341e4388ec28f907517b769a265'}"

        try:
            response = requests.get(url)
            json_data = json.loads(response.text)

            name = json_data['name']
            region = json_data['sys']['country']
            lat = json_data['coord']['lat']
            lon = json_data['coord']['lon']
            temp_c = json_data['main']['temp']
            temp_f = (temp_c * 9/5) + 32
            condition_text = json_data['weather'][0]['main']
            wind_mph = json_data['wind']['speed'] * 2.237
            wind_kph = json_data['wind']['speed']
            wind_degree = json_data['wind']['deg']
            wind_dir = json_data['wind']['deg']
            pressure_mb = json_data['main']['pressure']
            pressure_in = pressure_mb * 0.02952998751
            humidity = json_data['main']['humidity']

            return render_template('home.html', name=name, region=region, lat=lat, lon=lon, temp_c=temp_c, temp_f=temp_f,
                       condition_text=condition_text,
                       wind_mph=wind_mph, wind_kph=wind_kph, wind_degree=wind_degree,
                       wind_dir=wind_dir, pressure_mb=pressure_mb, pressure_in=pressure_in,
                       humidity=humidity)
        except:
            return render_template('home.html', error='Please enter a correct Place name...')
    else:
        return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
