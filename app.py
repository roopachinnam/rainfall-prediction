
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pickled model
with open('rain_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for the prediction result
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input values from the HTML form
    location = int(request.form['location'])
    min_temp = float(request.form['min_temp'])
    max_temp = float(request.form['max_temp'])
    wind_dir = float(request.form['wind_dir'])
    wind_speed = float(request.form['wind_speed'])
    humidity = float(request.form['humidity'])
    pressure = float(request.form['pressure'])
    cloud = float(request.form['cloud'])
    temp = float(request.form['temp'])
    today_rain = int(request.form['today_rain'])

    # Create a list of the input values
    input_values = [[location, min_temp, max_temp, wind_dir, wind_speed, humidity, pressure, cloud, temp, today_rain]]

    # Make a prediction using the model
    prediction = model.predict(input_values)

    # Convert the prediction to a string and return it
    if prediction == 0:
        result = "It'll not Rain Tomorrow"
    else:
        result = "It'll Rain Tomorrow"

    return render_template('index.html', prediction="{} in {}".format(result, location))

if __name__ == '__main__':
    app.run(debug=True)
app.py
Displaying app.py.
