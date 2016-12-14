from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def echo():
    return "This is my Flask Test Server"

if __name__ == '__main__':
    app.run(port=8000)
