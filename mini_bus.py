import requests
import pprint


line = {
		    '140M':['spiderman',"t'challa",'vision'],
			    '240M':['bucky','hawkeye','scarlet witch'],
			    '340M':['superman','mickey','duck','dog'] 
}


def check_stops(choose_bus):
	if choose_bus in line.keys():
		print(line[choose_bus])
	else:
		print("No This Line !")
		choose_bus=input("Which mini bus do u want?")
		check_stops(choose_bus)


def check_route(station_name):
	if station_name in line.values():
		print(line.keys())
		pprint.pprint("Thank you for searching !")
	else:
		pprint.pprint("We dont have mini_bus to go to your target place , sorry")

def check_option(option):
	if option=='1':
		choose_bus=input("Which mini bus do u want to search?")
		check_stops(choose_bus)
	elif option=='2':
		station_name=input("Which target station you want to go?")
		check_route(station_name)



pprint.pprint(line)


option = input("What do you want to search ?Enter the numbers(1/2)  1.Stops  2.Route number")
check_option(option)





 	







