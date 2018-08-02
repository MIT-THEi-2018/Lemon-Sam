import requests
import pprint


line = {
    '140m':['spiderman',"t'challa",'vision'],
	    '240m':['bucky','hawkeye','scarlet witch'],
	    '340m':['superman','mickey','duck','dog'] 
}


def check(choose_bus):
	if choose_bus in line.keys():
		print(line[choose_bus])
	else:
		print("No This Line !")
		choose_bus=input("Which mini bus do u want?")
		check(choose_bus)


pprint.pprint(line)

choose_bus=input("Which mini bus do u want?")
check(choose_bus)







