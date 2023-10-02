from flask import render_template, request
from app import app
import os
import smtplib

MY_EMAIL = os.getenv('MY_EMAIL')
APP_EMAIL = os.getenv('APP_EMAIL')
EMAIL_PASS = os.getenv('EMAIL_PASS')


def send_email(name, email, subject, message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(APP_EMAIL, EMAIL_PASS)
        connection.sendmail(from_addr=APP_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Portfolio Message\n\nName: {name}\nEmail: {email}\nSubject: {subject}\n{message}")


@app.route('/')
def home():
    return render_template('index.html', homepage=True)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data['name'], data['email'], data['subject'], data['message'])
        return render_template('contact.html', contact_page=True, sent_message=True)
    return render_template('contact.html', contact_page=True)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/project/<int:project_id>')
def project(project_id):
    return render_template('base-project.html', id=project_id)
