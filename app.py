from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def index():
    return "server is running.."


@app.post("/get_prediction")
def get_prediction():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'
