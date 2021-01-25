from tkinter import *
from time import sleep
from random import *
input()
interface=Tk()
screen=Canvas(interface,height=600,width=800,background="sky blue")
screen.pack()


rain_num=200
xr=[]
yr=[]
rain=[]
tilt=2
v=7
speeds=[]
lengths=[]
for i in range(rain_num):
    xr.append(randint(0,800))
    yr.append(randint(0,600))
    lengths.append(randint(2,5))
    speeds.append(randint(8,10))


for frame in range(10000):

    for i in range(rain_num):
        yr[i]+=speeds[i]
        xr[i]+=tilt
        if xr[i]<0:
            xr[i]=800
        elif xr[i]>800:
            xr[i]=0


        if yr[i]>600:
            yr[i]=0

        rain.append(screen.create_line(xr[i],yr[i],xr[i]+tilt,yr[i]+lengths[i],width=2,fill="white"))
        
    screen.update()
    sleep(0.03)

    for i in range(len(rain)):
        screen.delete(rain[i])
    rain=[]

print("done")


screen.mainloop()
