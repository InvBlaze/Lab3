from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_sysc3010():
    return "<p>SYSC3010 rocks!</p>"
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
