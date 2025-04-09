from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get("https://httpbin.org/ip")
    return f"Ваш IP: {r.json()['origin']}"

if __name__ == "__main__":
    app.run()
