import pyxel  
from math import *
from random import randint as ran, shuffle
def val(value, istart, istop, ostart, ostop):
	return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
def angle_between(a, b):
	angle = (atan2(a[1] - b[1], b[0] - a[0]))
	return radians(180-degrees(angle)) 
def frdist(x1,y1,x2,y2):
	dx = int(abs(x1-x2))
	dy = int(abs(y1-y2))
	return(hypot(dx, dy))


x= 0
y= 1
v= 2
c = 3
size = 500
goobabs = []
for i in range(200):
	goobabs.append([ran(0,size),ran(0,size),[0,0],ran(16,23)])	

class App:
	def __init__(self):
		pyxel.init(size, size,fps=60)
		pyxel.colors.append(0xff3333)
		pyxel.colors.append(0xff8833)
		pyxel.colors.append(0xffff33)
		pyxel.colors.append(0x33ff33)
		pyxel.colors.append(0x33ffff)
		pyxel.colors.append(0x3333ff)
		pyxel.colors.append(0xaa33ff)
		pyxel.colors.append(0xff33ff)
		pyxel.colors.append(0xffffff)
		self.p = goobabs
		pyxel.run(self.update, self.draw)
	def update(self):
		for p in self.p:
			p[x]+=p[v][x]
			p[y]+=p[v][y]
			p[v][x] *= 0.9
			p[v][y] *= 0.9

			if p[x] > size:
				p[v][x] = abs(p[v][x])*-1
				p[x] -= 1
			if p[y] > size:
				p[v][y] = abs(p[v][y])*-1
				p[y] -= 1
			if p[x] < 0:
				p[v][x] = abs(p[v][x])
				p[x] += 1
			if p[y] < 0:
				p[v][y] = abs(p[v][y])
				p[y] += 1
				
			for pp in self.p:
				if not pp == p:
					d = frdist(p[x],p[y],pp[x],pp[y])
					if 0 < d < 15:
						dx = p[x] - pp[x]
						dy = p[y] - pp[y]
						p[v][x] += (dx / d) / 3
						p[v][y] += (dy / d) / 3
					if 60 > d > 20 and (pp[c] in (p[c], p[c]-1)):
						dx = p[x] - pp[x]
						dy = p[y] - pp[y]
						p[v][x] -= (dx / d) / 6
						p[v][y] -= (dy / d) / 6
		if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
			self.p.append([pyxel.mouse_x,pyxel.mouse_y,[pyxel.rndi(-10,10),pyxel.rndi(-10,10)],pyxel.rndi(16,23)])
	def draw(self):
		pyxel.cls(0)
		pyxel.mouse(True)
		for p in self.p:
			pyxel.circ(p[x],p[y],5,p[c])
			
			

				
		

App()