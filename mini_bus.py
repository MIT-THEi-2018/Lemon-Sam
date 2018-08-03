from tkinter import *
import pprint

line = {
		    '140M':['Mongkok',"Charleen's home",'Prince Edward'],
			'240M':['Tsuen Wan','Sham Shui Po',"Joyce's Notebook"],
			'340M':["Leon's heart","Kwai Fong",'M.I.T',"Kowloon Tong","Nitah's Mobile"] 
}


def show_entry_fields():
	if e1.get() in line.keys():
	  	print(line[e1.get()])
	  	pprint.pprint("Thank you for using our System. ! SEE you !! YaY !!")	
	else:
	  	print("No This Line !")
	  	pprint.pprint("Thank you for using our System. ! SEE you !! YaY !!")

def show_entry_stops_fields():
	if e2.get() in line['140M']:
		print('140M')
		pprint.pprint("Thank you for using our System. ! SEE you !! YaY !!")
	elif e2.get() in line['240M']:	
		print('240M')
		pprint.pprint("Thank you for using our System. ! SEE you !! YaY !!")
	elif e2.get() in line['340M']:
		print('340M')
		pprint.pprint("Thank you for using our System. ! SEE you !! YaY !!")
	else:
		print("We dont have mini_bus to go to your destination , sorry")
		pprint.pprint("Thank you for using our System. ! SEE you !! YaY !!")	
   
#def clear_fields():
#	e1.get = ""
#	e2.get = ""

def clear():
    e1.delete(first=0,last=100)
    e2.delete(first=0,last=100)


master = Tk()
Label(master, text="Route Number").grid(row=0)
Label(master, text="Stops").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)



e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show stops', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Show route', command=show_entry_stops_fields).grid(row=3, column=2, sticky=W, pady=4)
Button(master, text='Clear', command=clear).grid(row=3, column=3, sticky=W, pady=4)



mainloop( )