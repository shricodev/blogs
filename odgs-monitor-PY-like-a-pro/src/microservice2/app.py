import random

import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)


def get_gh_users():
    url = "https://api.github.com/users?per_page=5"

    # Choose a random timeout between 1 and 5 seconds
    timeout = random.randint(3, 6)

    # Make a GET request to the URL and return the response or an error message
    try:
        response = requests.get(url, timeout=timeout)
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request timed out after {} seconds".format(timeout)}
    except requests.exceptions.RequestException as e:
        return {"error": "Request failed: {}".format(e)}


# Define a route for the microservice
@app.route("/get-gh-users")
def get_users():
    # Create an empty list to store the results
    results = []

    # Loop through the number of requests and append the results to the list
    for _ in range(3):
        result = get_gh_users()
        results.append(result)

    # Return the list of results as a JSON response
    return jsonify(results)


@app.route("/")
def index():
    return "<p>Welcome to Flask microservice 2</p>"


@app.route("/health")
def health():
    return jsonify(status="Microservice 2 Running...")


@app.route("/os-details")
def details():
    try:
        response = requests.get("http://microservice1:5000/user-details").json()
        host_name = response["hostname"]
        host_ip = response["hostip"]
        return render_template("index.html", hostname=host_name, hostip=host_ip)
    except requests.exceptions.Timeout as errt:
        return {"error": "Request timed out after {} seconds".format(errt)}
    except requests.exceptions.RequestException as e:
        return {"error": "Request failed: {}".format(e)}


if __name__ == "__main__":
    app.run("0.0.0.0", 5001)
