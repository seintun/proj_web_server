from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your Raspberry Pi's IP
RASPBERRY_PI_IP = "XXX.XXX.XXX.XXX"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/trigger", methods=["POST"])
def trigger():
    try:
        # Send a request to Raspberry Pi to perform an action
        response = requests.get(f"http://{RASPBERRY_PI_IP}:5001/action")
        return {"status": "success", "response": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
