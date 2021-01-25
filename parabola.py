from time import sleep
from tkinter import *
from random import *
input("Press enter to start animation")

Interface = Tk()
screen = Canvas(Interface, width=1000, height=1000, background="black")
screen.pack()
ha=300
n=300
asdf=3
for i in range(1,900):
	#Top righ quadrant:
	x2=ha+i*asdf
	y1=i*asdf
	screen.create_line(ha,y1,x2,ha,fill="green")
	
	#Top left quadrant
	x2=ha-i*asdf
	y1=i*asdf
	screen.create_line(ha,y1,x2,ha,fill="white")
	

	#Bottom left quadrant:
	x2=ha-i*asdf
	y1=2*ha-i*asdf
	screen.create_line(ha,y1,x2,ha,fill="cyan")

	#Bottom right quadrant
	x2=ha+i*asdf
	y1=2*ha-i*asdf
	screen.create_line(ha,y1,x2,ha,fill="pink")
	sleep(0.01)
	screen.update()
	
screen.mainloop()
