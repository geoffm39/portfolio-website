from flask import render_template, redirect, url_for
from app import app


@app.route('/')
def home():
    return render_template('index.html', homepage=True)


@app.route('/contact')
def contact():
    return render_template('contact.html', contact_page=True)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/project/<int:project_id>')
def project(project_id):
    return render_template('base-project.html', id=project_id)
