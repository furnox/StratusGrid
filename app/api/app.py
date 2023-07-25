'''
    Flask app runner
'''
from flask import Flask, send_from_directory
from flask_restful import Api
import api as AppApi

app = Flask(__name__, static_url_path="", static_folder="../ui/build")
# CORS(app)
api = Api(app)

@app.route("/")
def root():
    '''
        Routing for root react request
    '''
    return send_from_directory(app.static_folder,"index.html")

api.add_resource(AppApi.Car, "/api/car")
api.add_resource(AppApi.Car, "/api/car/<int:car_id>", endpoint='delete')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
