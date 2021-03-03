from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python! This is version 2"

@app.route("/get")
def getDetails():
	return "This is a set of details we would like you to have"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
