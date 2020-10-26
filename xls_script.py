import xlrd, xlwt
import datetime

timer = str(datetime.datetime.today())
print(timer)

class Xls:
	
	def xls_output(list_):

		wb = xlwt.Workbook()
		ws = wb.add_sheet('Test')
		
		counter = 0
		counter_2 = 0
		quad_counter = 0



		for i in list_:

			if quad_counter != 3:

				ws.write(counter_2,counter,i)
				counter += 1
			
			if quad_counter == 3:

				ws.write(counter_2,counter,i)
				counter = 0
				counter_2 +=1
				quad_counter = -1

			quad_counter += 1
		stringer = 'D:\\python\\parse\\exel_base\\xl' + timer[12:13] + timer[14:16] + timer[17:19] + '.xls'
		print(stringer)

		wb.save(str(stringer))

