from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/grooming')
def grooming():
    return render_template('grooming.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/pets')
def pets():
    return render_template('pets.html')

@app.route('/help')
def help():
    return render_template('help.html')
