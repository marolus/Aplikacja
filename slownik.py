
#from Tkinter import Tk
#from tkFileDialog import askopenfilename
#Tk().withdraw()
import csv
def make_dict():
    slownik = {}
    path=open('C:/Users/HP/Documents\gatunki.csv','r')
    for line in path:
        if len(line) > 1:
            z = line.split()
            if z[0] != '':
                slownik[z[0]] = z[1]
    return slownik
print (make_dict())
