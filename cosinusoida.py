from time import sleep
from math import sin, cos
from os import system
colors = ["\033[95m", "\033[36m", "\033[91m", "\033[92m", "\033[94m", "\033[45m"]
p = 0
c = 0
SIZE = 60
HORIZSIZE = 250
screen = []
for _ in range(HORIZSIZE):
    screen.append([" "]*SIZE)

def reset_scr():
    for x in range(HORIZSIZE):
        for y in range(SIZE):
            screen[x][y] = " "
reset_scr()

def printscreen():
    for i in range(SIZE):
        string = ""
        for j in range(HORIZSIZE):
            string += screen[j][i]
        print(string)
        

AMPLIF = 1
COLCODESDIV = len(colors) - 1
while True:
    reset_scr()
    print(colors[c%COLCODESDIV], end="")
    for x in range(1, HORIZSIZE):
        innersin = ((sin( (x/10) + (p/10) )) + 1) / (2*AMPLIF)
        # print(innersin)
        y = int(innersin*SIZE)
        xj = HORIZSIZE - x-1
        yj = SIZE - y-1
        screen[xj][yj] = "*"
    printscreen()
    if p % 100 == 0: c+=1
    p += 1
    sleep(0.03)
    system("clear")
