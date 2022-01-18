import os
import logging
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    logging.debug("saying hello2")
    return 'Hello Joshua! Procfile test. '
