


line = {
		    '140M':['spiderman',"t'challa",'vision'],
			'240M':['bucky','hawkeye','scarlet witch'],
			'340M':['superman','mickey','duck','dog'] 
}
def check_route(choose_bus):
	if choose_bus in line.values():	
		print("TRUE")
	else:
		print("false")
print(line['140M'])
choose_bus=input("Which mini bus do u want to search?")
check_route(choose_bus)

