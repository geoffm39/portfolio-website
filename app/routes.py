from flask import render_template, redirect, url_for
from app import app


@app.route('/')
def home():
    return render_template('index.html', homepage=True)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/project')
def project():
    return render_template('single-portfolio.html')
