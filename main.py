from parser_script import Autoru_parser as Ap
from database_script import Database as Db

connection = Db.create_connection("D:/python/parse/sm_app.sqlite")

creator = Db.create_car_table()

Db.execute_query(connection,creator)


def car_massive_function(car_name):
	
	return Ap.parse(car_name)



def read():

	select_users = "SELECT price, model, year from cars"

	cars = Db.execute_read_query(connection,select_users)

	return cars


def record(name, price, year):

	car_creator = Db.create_cars(name, price, year)

	Db.execute_query(connection,car_creator)


def database_recorder(car_name):

	car_massive = car_massive_function(car_name)

	border = len(car_massive) / 3

	for i in range(0,int(border),3):
		
		record(car_massive[i],car_massive[i + 1], car_massive[i + 2])


def main():
	
	#database_recorder("camry")
	
	car_mas = read()

	for i in car_mas:
		print(i)
	


if __name__=="__main__":
	main()