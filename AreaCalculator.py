'''
		This area calculator can compute the area of a 
    given shape, as selected by the user. The 
    calculator will be able to determine the area 
    of the following shapes: Circle & Triangle.
'''

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "The calculator is starting up."
print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct unit"
option = raw_input("Enter C for Circle or T for Triangle: ").upper()

if option == "C":
    radius = float(raw_input("Enter the radius: "))
    area = pi*(radius**2)
    print "The pie is baking..."
    sleep(1)
    print "%.2f\n%s" % (area, hint)
elif option == "T":
    base = float(raw_input("Enter the base: "))
    height = float(raw_input("Enter the height: "))
    area = 0.5*base*height
    print "Uni Bi Tri.."
    sleep(1)
    print "%.2f\n%s" % (area, hint)
else:
    print "Error inout, the program exits."
