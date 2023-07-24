from flask_restful import Api, Resource, reqparse
import json
import psycopg2

connection = psycopg2.connect(database="stratusgrid",
  host="localhost",
  user="postgres",
  password="postgres",
  port="5432")
connection.autocommit = True  
cursor = connection.cursor()

class Car(Resource):
  def get(self):
    cursor.execute("SELECT * FROM car;")
    cars = cursor.fetchall()
    return [{"make": car[1], "model": car[2]} for car in cars]

  def post(self):
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

    sql = f"INSERT INTO car (make, model) VALUES(%s, %s);"
    cursor.execute(sql, (car["make"], car["model"]))