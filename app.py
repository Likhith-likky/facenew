from flask import Flask
from main import *

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"
    # fun()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)