from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from views import *

if __name__ == '__main__':

    app.run(debug=True)