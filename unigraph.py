from time import sleep
from math import sin, cos, tan
from os import system
import platform
colors = ["\033[95m", "\033[97m", "\033[91m", "\033[92m", "\033[94m", "\033[45m"]
p = 0
c = 0
SYST = platform.system() == "Windows"
SIZE = 40
HORIZSIZE = 150
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
    if SYST: sleep(0.2);system("cls")
    else: sleep(0.03); system("clear")

AMPLIF = 14
TA = 50

while True:
    reset_scr()
    print(colors[c%COLCODESDIV], end="")
    for x in range(0, HORIZSIZE):
        for y in range(0, SIZE):
            f = ((x-60-int(15*cos(p/TA)))**2 + (y-15-int(15*cos(p/TA)))**2 <= 100)
            g = int(tan(x+p/TA)*abs(cos(x))*sin(p/TA)) == y
            h = abs(x-(p%100)) + abs(y-5) <= 36
            if h:
                screen[HORIZSIZE-x-1][SIZE-y-1] = colors[4]+"#"+colors[1]
            if f:
                screen[HORIZSIZE-x-1][SIZE-y-1] = colors[0]+"*"+colors[1]
            if g:
                screen[HORIZSIZE-x-1][SIZE-y-1] = colors[3]+"0"+colors[1]
    printscreen()
    if p % 100 == 0: c+=1
    p += 1
    
