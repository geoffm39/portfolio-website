from flask import render_template, redirect, url_for
from app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')
