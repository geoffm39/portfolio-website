from flask import Flask
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)

from app import routes

if __name__ == '__main__':
    app.run()
