from flask import Flask
app = Flask(__name__)


@app.route("/")
def hellow_wirld():
    return "hello world"

@app.route('/name/<text>')
def name(text):
    return "hello "+text


if __name__ == '__main__':
    app.run()