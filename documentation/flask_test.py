https://flask.palletsprojects.com/en/3.0.x/installation/

#$ pip install Flask

# Example of using flask
https://pypi.org/project/Flask/
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"