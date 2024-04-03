from math import cos
from math import sin
from time import sleep

colors = ["\033[95m", "\033[93m", "\033[91m", "\033[92m", "\033[94m"]
k = 0
c = 0

while True:
	print(colors[c%4], end="")
	print(" " * int(abs(100 * sin(k/100))), end="*****")
	print(colors[(c+1)%4], end="")
	print(" " * int(abs(100 * cos(k/100-100))), end="*****\n")
	sleep(0.01)
	if k % 100 == 0: c += 1
	k += 1

