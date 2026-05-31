# Minimal application placeholder
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return {"status": "online"}, 200