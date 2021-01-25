from time import sleep
from tkinter import *
from math import *
screen=Canvas(height=600,width=800,background="white")
screen.pack()



def create_elipse(xcenter,ycenter,frequency,r,small_r,increase,color,screen):
    points=[]
    for f in range(300):
        x=xcenter+r*cos(f*frequency)
        y=ycenter-r*sin(f*frequency)
        r+=increase
        points.append(screen.create_oval(x-small_r,y-small_r,x+small_r,y+small_r,fill=color))
    return points

xcenter=400
ycentre=300
frequency=0.1
r=1
small_r=5
increase=0.5


mainf=0.1
x=xcenter
y=ycentre
br=r+300*increase
ros=100

for frame in range(100000):
    # line=screen.create_line(x,0,x,600,width=1)
    # line2=screen.create_line(0,y,800,y,width=1)
    #outline=screen.create_oval(x-br,y-br,x+br,y+br,fill="blanched almond",outline="blanched almond",width=4)

    spiral_list=create_elipse(x,y,frequency,r,small_r,increase,"black",screen)


    screen.update()
    sleep(0.01)
    screen.delete("all")
    for oval in spiral_list:
        screen.delete(oval)
    #screen.delete(outline)
    frequency+=0.001



    x = xcenter + ros * cos((mainf * frame))
    y = ycentre - ros * sin((mainf * frame))
    if y < ycentre:
        y = 2 * ycentre - y

    # screen.delete(line)
    # screen.delete(line2)
print("done")
screen.mainloop()



#Generating a circle and it's points:
"""r=200
point_num=90
angle=(2*pi)/point_num

xp=[]
yp=[]
for i in range(point_num):
    alpha=i*angle
    xp.append(xc-cos(alpha)*r)
    yp.append(yc-r*sin(alpha))
newr=3
for i in range(len(xp)):
    screen.create_oval(xp[i]-newr,yp[i]-newr,xp[i]+newr,yp[i]+newr,fill="black")"""
