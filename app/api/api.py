'''
    Handles all API calls
'''
import json
from flask_restful import Resource, reqparse
import database


class Car(Resource):
    '''
        Handles all car resource interactions
    '''
    def delete(self, car_id):
        '''
            Deletes a single car
        '''
        database.delete_car(car_id)

    def get(self):
        '''
            Retrieves all cars
        '''
        cars = database.get_all_cars()
        return [{"id": car[0], "make": car[1], "model": car[2]} for car in cars]

    def post(self):
        '''
            Adds a single car
        '''
        parser = reqparse.RequestParser()
        parser.add_argument("data", type=str)

        args = parser.parse_args()
        data = args["data"]

        try:
            car = json.loads(data)
        except:
            print("Data is not valid json")
            return

        if "make" not in car or "model" not in car:
            print("Data is not valid")
            return

        database.add_one_car(car)
