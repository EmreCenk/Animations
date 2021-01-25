#DNA like animation thing:
from time import sleep
sleeptime=0.0001
while True:
    for i in range(0,61):
        star=60-i
        sleep(sleeptime)
        print(i*"*"+"bbbb"+star*"*")
        star=60-i
        sleep(sleeptime)
        
        print(star*"*"+"aaaa"+i*"*")
