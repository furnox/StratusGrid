'''
    Database access layer
'''
import psycopg2

connection = psycopg2.connect(
  database="stratusgrid",
  host="sgdata",
  user="postgres",
  password="postgres",
  port="5432")
connection.autocommit = True
cursor = connection.cursor()

def get_all_cars():
    '''
        SELECT all cars
    '''
    sql = "SELECT * FROM car;"
    cursor.execute(sql)
    return cursor.fetchall()

def add_one_car(car):
    '''
        INSERT one car
    '''
    sql = "INSERT INTO car (make, model) VALUES(%s, %s);"
    cursor.execute(sql, (car["make"], car["model"]))

def delete_car(car_id):
    '''
        DELETE one car
    '''
    sql = "DELETE FROM car WHERE id = %s;"
    cursor.execute(sql, (car_id,))
