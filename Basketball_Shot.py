########################################################################
#
#
#Created By: Emre Cenk
#Last updated: October 12, 2020
#
##########################################################################
from time import sleep
from tkinter import *
interface=Tk()
screen=Canvas(interface,width=800,height=600,background="sky blue")
screen.pack()

#Creating background:
cfl=500
floor=screen.create_rectangle(0,cfl,800,600,fill="grey")


pole_height=305
pole_w=10
px=650

#Net holding bridge piece:
bridgew=50
bridgeh=5

#Backboard:
b_h=74
b_w=7

#Rim
rimh=4
rimw=60
calibrate=2

#Net initial coordinates:
asdf=[px-bridgew-rimw,cfl-pole_height+bridgeh-(rimh/2)-calibrate,px-bridgew,
                       cfl-pole_height+bridgeh+(rimh/2)-calibrate]
netx1=asdf[0]
nety1=asdf[1]
netx2=asdf[2]
nety2=asdf[3]
#screen.create_line(540, 196, 560,246)

rim=screen.create_oval(px-bridgew-rimw,cfl-pole_height+bridgeh-(rimh/2)-calibrate,px-bridgew,
                       cfl-pole_height+bridgeh+(rimh/2)-calibrate,
                       outline="red",width=3)
net_pole=screen.create_rectangle(px,cfl-pole_height,px+pole_w,cfl,fill="black")

bridge=screen.create_rectangle(px-bridgew-b_w,cfl-pole_height,px,cfl-pole_height+bridgeh,fill="black")

backboard=screen.create_rectangle(px-b_w-bridgew,  cfl-pole_height-b_h,  px-bridgew,  cfl-pole_height+bridgeh,
                                  fill="white")

player_height=180
legh=player_height/2
legbodinter=125

headh=40
headw=35

bodyh=(player_height/2)-headh

armyplus=0
armlength=60
go=True
f=0
v=0
calibrate_ball=20

# noinspection PyRedeclaration
legh = 45
arm1 = screen.create_line(legbodinter, cfl - legh - bodyh, legbodinter + armlength,
                          cfl - legh - bodyh + armyplus, width=2)
leg1 = screen.create_line(legbodinter - 25, cfl, legbodinter, cfl - legh, fill="black", width=2.5)
leg2 = screen.create_line(legbodinter, cfl - legh, legbodinter + 25, cfl, fill="black", width=2.5)
body = screen.create_line(legbodinter, cfl - legh, legbodinter, cfl - legh - bodyh, width=2)

head = screen.create_oval(legbodinter - (headw / 2), cfl - legh - bodyh - headh, legbodinter + (headw / 2),
                          cfl - legh - bodyh, width=2, fill="sky blue")
arm2 = screen.create_line(legbodinter, cfl - legh - bodyh, legbodinter + armlength,
                          cfl - legh - bodyh + 30 + armyplus, width=2)
ball = screen.create_oval(legbodinter + armlength - calibrate_ball + v, cfl - legh - bodyh + armyplus,
                          legbodinter - calibrate_ball + armlength + 30 + v, cfl - legh - bodyh + 30 +
                          armyplus, fill="orange")
legh = player_height / 2
person = [leg1, leg2, head, body, arm1, arm2]
screen.update()
sleep(1)
for x in person:
    screen.delete(x)
screen.delete(ball)
v=0
basketin=False
w=1
delrim=False
while go:


    arm1 = screen.create_line(legbodinter, cfl - legh - bodyh, legbodinter + armlength,
                              cfl - legh - bodyh + armyplus, width=2)
    leg1 = screen.create_line(legbodinter - 25, cfl, legbodinter, cfl - legh, fill="black", width=2)
    leg2 = screen.create_line(legbodinter, cfl - legh, legbodinter + 25, cfl, fill="black", width=2)
    body = screen.create_line(legbodinter, cfl - legh, legbodinter, cfl - legh - bodyh, width=2)

    head = screen.create_oval(legbodinter - (headw / 2), cfl - legh - bodyh - headh, legbodinter + (headw / 2),
                              cfl - legh - bodyh, width=2, fill="sky blue")
    arm2 = screen.create_line(legbodinter, cfl - legh - bodyh, legbodinter + armlength,
                              cfl - legh - bodyh + 30 + armyplus, width=2)
    if basketin==False:
        if f <= 5:
            ball = screen.create_oval(legbodinter + armlength - calibrate_ball, cfl - legh - bodyh + armyplus,
                                      legbodinter - calibrate_ball + armlength + 30, cfl - legh - bodyh + 30 + armyplus,
                                      fill="orange")
        else:
            #The first time the ball is here, the coordinates of it are:[171, 193.0, 201, 223.0]
            v += 20
            x_ball = 171 + v
            y_ball = 0.6 * f ** 2 - 15 * f + 193
            ball = screen.create_oval(x_ball, y_ball, x_ball + 30, y_ball + 30,fill="orange")
            if 555<=x_ball<=605 :
                basketin=True

    else:
        if f<36:
            w+=1
            y_ball+=0.5*w**2
            ball = screen.create_oval(x_ball, y_ball, x_ball + 30, y_ball + 30, fill="orange")

            rim = screen.create_oval(px - bridgew - rimw, cfl - pole_height + bridgeh - (rimh / 2) - calibrate,
                                     px - bridgew,
                                     cfl - pole_height + bridgeh + (rimh / 2) - calibrate,
                                     outline="red", width=3)
            backboard = screen.create_rectangle(px - b_w - bridgew, cfl - pole_height - b_h, px - bridgew,
                                                cfl - pole_height + bridgeh,
                                                fill="white")
            delrim=True
        else:

            ball = screen.create_oval(x_ball, cfl-30, x_ball + 30, cfl, fill="orange")


    screen.update()
    sleep(0.1)
    if f<=10:
        armyplus-=6

    if f<=9:
        legbodinter+=1

    if f<=8:
        cfl-=0.2*f**2 - 12*f + 50
    else:
        cfl=500
    person=[leg1,leg2,head,body,arm1,arm2]
    for organ in person:
        screen.delete(organ)
    screen.delete(ball)
    if delrim:
        screen.delete(rim)

    f+=1

arm1 = screen.create_line(legbodinter,  cfl-legh-bodyh,  legbodinter+armlength,  cfl-legh-bodyh+armyplus ,width=2)
leg1 = screen.create_line(legbodinter - 25, cfl, legbodinter, cfl - legh, fill="black", width=2)
leg2 = screen.create_line(legbodinter, cfl - legh, legbodinter + 25, cfl, fill="black", width=2)
body = screen.create_line(legbodinter, cfl - legh, legbodinter, cfl - legh - bodyh, width=2)

head = screen.create_oval(legbodinter - (headw / 2), cfl - legh - bodyh - headh, legbodinter + (headw / 2),
                          cfl - legh - bodyh, width=2,fill="sky blue")
arm2 = screen.create_line(legbodinter,  cfl-legh-bodyh,  legbodinter+armlength,  cfl-legh-bodyh+30+armyplus,width=2)



screen.mainloop()
