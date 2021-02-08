from flask import Flask, render_template
import apiRequest as ap

app = Flask(__name__)
@app.route("/")
def pg():
	return render_template('marsWeather.html')
@app.route("/marsJson")
def pgJ():
	return render_template('mars.json')