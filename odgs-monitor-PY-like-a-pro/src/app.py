import socket

from flask import Flask, jsonify, render_template

app = Flask(__name__)


def user_os_details():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return hostname, hostip


@app.route("/")
def index():
    return "<p>Welcome to Flask webapp</p>"


@app.route("/health")
def health():
    return jsonify(status="Running...")


@app.route("/user-os-details")
def details():
    host_name, host_ip = user_os_details()
    return render_template("index.html", hostname=host_name, hostip=host_ip)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
