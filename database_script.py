import sqlite3
from sqlite3 import Error


class Database:

    def create_connection(path):
        
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    
    def execute_query(connection, query):
        
        cursor = connection.cursor()
        
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")


    def create_car_table():

        table_creator = """
        CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        price INTEGER,
        year INTEGER
        );"""

        return table_creator

       
    def create_cars(model,price,year):

        car_insert = """INSERT INTO
        cars (model, price, year)
        VALUES
        (""" + "'" + str(model) +"'"+ "," + str(price) + "," + str(year) + ")"

        return car_insert

    
    def execute_read_query(connection, query):
        
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    






