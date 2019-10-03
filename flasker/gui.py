from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def _index():
    return "Index"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def get_member(name):
    return f"Name {name.capitalize()}"


if __name__ == "__main__":
    app.run()