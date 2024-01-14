from flask import Flask, request, url_for, redirect, render_template, flash, get_flashed_messages
from werkzeug.datastructures import ContentRange
import requests, json
import os
from werkzeug.utils import secure_filename
from flask_wtf import RecaptchaField, FlaskForm
import numpy as np
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('trypage.html')
@app.route('/about_us')
def about():
    return render_template('newpage.html')
@app.route('/sanitaryware')
def sanitaryware():
    return render_template('sanitaryware.html')
@app.route('/contact_us')
def pls():
    return render_template('contact_us.html')
@app.route('/hardware')
def hardware():
    return render_template('Hardware.html')

if __name__ == "__main__":
    app.run(debug=True)