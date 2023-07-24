from flask import Flask, send_from_directory
from flask_restful import Api
import api.api as AppApi

app = Flask(__name__, static_url_path="", static_folder="ui/build")
# CORS(app)
api = Api(app)

@app.route("/")
def root():
    return send_from_directory(app.static_folder,"index.html")

api.add_resource(AppApi.Car, "/api/car")
