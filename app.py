from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "server is running.."


@app.post("/get_prediction")
def get_prediction():
    return "post req.."
