import requests
import pprint


line = {
		    '140M':['Mongkok',"Charleen's home",'Prince Edward'],
			'240M':['Tsuen Wan','Sham Shui Po',"Joyce's Notebook"],
			'340M':["Leon's heart","Kwai Fong",'M.I.T',"Kowloon Tong","Nitah's Mobile"] 
}


def check_stops(choose_bus):
	if choose_bus in line.keys():
		print(line[choose_bus])
	elif choose_bus == 'quit':
		print('OK!')
	else:
	 print("No This Line !")



def check_route(station_name):
	if station_name in line['140M']:
		print('140M')
	elif station_name in line['240M']:	
		print('240M')
	elif station_name in line['340M']:
		print('340M')
	elif station_name == 'quit':
		print('OK!')
	else:
		print("We dont have mini_bus to go to your destination , sorry")	


def check_option(option):
	if option=='1':
		choose_bus=input("Which mini bus do u want to search?")
		check_stops(choose_bus)
	elif option=='2':
		station_name=input("Which target station you want to go?")
		check_route(station_name)
	else:	
		print("No this option")



option = input("What do you want to search ?Enter the numbers(1/2)  1.Stops  2.Route number")
check_option(option)

print("Thank you for searching !")



 	







