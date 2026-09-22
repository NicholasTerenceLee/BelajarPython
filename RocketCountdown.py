import time as t
import sys
x=5
print ("Rocket Launching in : ")

for i in range (5):
    t.sleep(1)
    print(x)
    x -= 1

    if x == 0:
        comt = "GOOOOOOOOOOOOOOOOOOOOOOOON"
        for char in comt:
            t.sleep(0.025)
            sys.stdout.write(char)


   

