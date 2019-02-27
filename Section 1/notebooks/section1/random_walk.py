import random
from time import sleep

def random_walk(n):
	"""Return coordinates after random walk of 'n' steps"""
	x = 0
	y = 0
	for i in range(n):
		step = random.choice(["N", "S", "E", "W"])
		if step == "N":
			y += 1
		elif step == "S":
			y -= 1
		elif step == "E":
			x += 1
		else:
			x -= 1
	return(x, y)
	
for i in range(25):
	walk = random_walk(10)
	sleep(0.5)
	print(walk, "Distance from pub = ", abs(walk[0]) + abs(walk[1]))


def random_walk_alt(n):
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0,1), (0, -1), (1, 0), (-1, 0)])
		x += dx
		y += dy
	return (x, y)
	
for i in range(25):
	walk = random_walk_alt(10)
	print(walk, "Distance from pub = ", abs(walk[0]) + abs(walk[1]))		
