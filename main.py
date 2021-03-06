from parser_script import Autoru_parser as Ap
from database_script import Database as Db
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from parser_interface import Ui_MainWindow 
from xls_script import Xls
import datetime


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()

script_dir = os.getcwd()
connection = Db.create_connection(script_dir +  "\\sm_app.sqlite")

directory = 'exel_base' 
path = os.path.join(script_dir, directory) 

dete = str(datetime.datetime.now())

try: 
	os.mkdir(path) 
except FileExistsError : 
	pass


def create_new_table():
	
	creator = Db.create_car_table()
	Db.execute_query(connection,creator)

	
def car_massive_function(car_name):
	
	return Ap.parse(car_name)


def read(select):

	cars = Db.execute_read_query(connection,select)
	return cars


def record(name, price, year):

	car_creator = Db.create_cars(name, price, year)
	Db.execute_query(connection,car_creator)


def database_delete():

	deleter = 'DROP TABLE cars'
	Db.execute_query(connection,deleter)


def database_recorder():

	database_delete()
	create_new_table()
	current_car = str(ui.comboBox.currentText())
	car_massive = car_massive_function(current_car)
	writer_massive = []
	border = len(car_massive)
	counter = 0

	for i in range(0,int(border),3):

		counter += 1
		record(car_massive[i],car_massive[i + 1], car_massive[i + 2])

	show_carlist()
	year_beg = str(ui.lineEdit.text())
	year_end = str(ui.lineEdit_2.text())

	if year_beg == '':
		year_beg = '1912'
	if year_end == '':
		year_end = dete[0:4]

	xls_writer_list = read('SELECT id, model, price, year FROM cars WHERE year BETWEEN '+ year_beg + ' AND ' + year_end )
	
	for i in xls_writer_list:
		for it in i:
			writer_massive.append(it)

	print(writer_massive)
	Xls.xls_output(writer_massive)

	
def show_carlist():

	year2_beg = str(ui.lineEdit.text())
	year2_end = str(ui.lineEdit_2.text())

	print(year2_beg)

	if year2_beg == '':
		year2_beg = '1912'
	if year2_end == '':
		year2_end = dete[0:4]

	ui.listWidget.clear()
	viewlist = read('SELECT id, model, price, year FROM cars WHERE year BETWEEN '+ year2_beg + ' AND ' + year2_end )
	str_viewlist = [str(i) for i in viewlist]
	digit_counter = 0	
	
	for i in str_viewlist:
		digit_counter += 1
		ui.listWidget.addItem(i)

	ui.lcdNumber.display(digit_counter)


def main():
	
	ui.setupUi(MainWindow)
	MainWindow.show()

	carnamelist = ['vesta','focus','camry','a4']
	for i in carnamelist:
		ui.comboBox.addItem(i)
	create_new_table()
	ui.pushButton.clicked.connect(database_recorder)
	
	sys.exit(app.exec_())

	
if __name__ == "__main__":
	main()
