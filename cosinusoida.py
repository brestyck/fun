from time import sleep
from math import sin, cos, tan
from os import system
colors = ["\033[95m", "\033[97m", "\033[91m", "\033[92m", "\033[94m", "\033[45m"]
p = 0
c = 0
SIZE = 60
HORIZSIZE = 250
COLCODESDIV = len(colors) - 1
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
        

AMPLIF = 8

while True:
    reset_scr()
    print(colors[c%COLCODESDIV], end="")
    for x in range(1, HORIZSIZE):
        zinnersin = tan( (x/AMPLIF) + (p/10) )
        innersin = (zinnersin + 1) / (2)
        print(innersin)
        y = int((innersin)*SIZE)
        print(y)
        xj = HORIZSIZE - x-1
        yj = SIZE - y-1
        if xj >= 0 and xj < HORIZSIZE and yj >= 0 and yj < SIZE:
            screen[xj][yj] = "*"
    printscreen()
    if p % 100 == 0: c+=1
    p += 1
    sleep(0.03)
    system("clear")
