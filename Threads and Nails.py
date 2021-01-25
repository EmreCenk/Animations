from tkinter import *
from time import sleep
from math import *
input("Press enter to start animation.")
interface=Tk()
screen=Canvas(interface,height=600,width=800,background="white")
screen.pack()


xc=400
yc=300
r=200
point_number=200
delta_angle=(2*pi)/point_number

w=4

coordinates=[]
for i in range(point_number):
    angle=i*delta_angle
    x=xc+r*cos(angle)

    y=yc-sin(angle)*r
    screen.create_oval(x,y,x+w,y+w,fill="black")
    coordinates.append([x,y])

skip=200
for i in range(len(coordinates)):
    x1=coordinates[i][0]
    y1=coordinates[i][1]


    x2=coordinates[(i+skip)%len(coordinates)][0]
    y2=coordinates[(i+skip)%len(coordinates)][1]
    screen.create_line(x1,y1,x2,y2)
    screen.update()
    sleep(0.005)
    #Circle art:
    if i%2==0:
        skip=skip*5
    else:
        skip-=50


screen.mainloop()

