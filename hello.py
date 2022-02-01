import os
import logging
from flask import Flask

# new
import dotenv
from dotenv import load_dotenv

# new
load_dotenv()

# new
token = os.getenv('TOKEN')


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    logging.debug("saying hello")
    return 'Hello world ' + token # + token new
