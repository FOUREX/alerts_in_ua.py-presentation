import base64
from os import getenv

from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from alerts_in_ua.alerts_client import AlertsClient

load_dotenv("../.env")

app = Flask(__name__)
alerts_client = AlertsClient(getenv("ALERTS_CLIENT_TOKEN"))


@app.route("/api/get_active", methods=["GET"])
def get_active():
    locations = alerts_client.get_active()
    image = locations.render_map()

    image_base64 = base64.b64encode(image.getvalue()).decode("utf-8")
    locations_list = locations.location_title

    return jsonify({"locations": locations_list, "image": image_base64})


@app.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
