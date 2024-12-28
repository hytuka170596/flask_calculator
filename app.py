import os
from flask import Flask, render_template

APP = Flask(__name__)
HOST = "90.156.225.70"
PORT = 5050
SERVICE_NAME = "application"
ADMIN_NAME = os.environ.get("ADMIN_NAME", "admin")


@APP.route("/brigada7")
def create_table():
    return render_template("index.html")



if __name__ == "__main__":
    APP.run(host=HOST, port=PORT)
