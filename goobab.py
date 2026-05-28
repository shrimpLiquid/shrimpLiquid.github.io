import pyxel  
from math import *
from random import randint as ran, shuffle
def val(value, istart, istop, ostart, ostop):
	return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
def angle_between(a, b):
	angle = (atan2(a[1] - b[1], b[0] - a[0]))
	return radians(180-degrees(angle)) 
def vector_between(a,b,d):
	if d != 0:
		v = (b[1] - a[1], b[0] - a[0])
		return(((v[1]/d)*-1,(v[0]/d)*-1)) 
	return((0,0))
def mag(d,ma):
	if d <= 20:
		return(val(d,0,20,-1,0))
	elif d < 100:
		return(val(d,20,100,1*ma,0))
	elif d >= 100 and d < 200:
		return(val(d,100,200,0,1*ma))
	else:
		return(0)
def apply_actration(vi,f,m,distace):
	distace = mag(distace,m/10)
	return([vi[0]+f[0]*distace,vi[1]+f[1]*distace])
def spawn(num,colour):
	for i in range(num):
		f.append([ran(0,599),ran(0,599),[0,0],colour])
x= 0
y= 1
v= 2
c = 3

f =[]  
"""spawn(10,1)
spawn(10,2)"""
#random.seed(1)

for i in range(200):
	f.append([ran(0,599),ran(0,599),[0,0],ran(1,8)])	
global rules
rules = {
	}

for Y in range(8):
	rules[(Y+1,Y+1)]=1
	rules[(Y+2,Y+1)]=1
"""for p1 in range(8):
	for p2 in range(8):
		if p1 != p2:
			rules[(p1+1,p2+1)]=ran(-1,1)/2"""
class App:
	def __init__(self):
		pyxel.init(600, 600,fps=600)
		pyxel.colors[1] = 0xff3333
		pyxel.colors[2] = 0xff8833
		pyxel.colors[3] = 0xffff33
		pyxel.colors[4] = 0x33ff33
		pyxel.colors[5] = 0x33ffff
		pyxel.colors[6] = 0x3333ff
		pyxel.colors[7] = 0xaa33ff
		pyxel.colors[8] = 0xff33ff
		pyxel.colors[9] = 0xffffff
		self.p = []
		self.rules=rules
		self.dist = 0
		self.th = []
		self.display = 0
		for i in f:
			self.p.append(i)  
		pyxel.run(self.update, self.draw)
	def update(self):
		if pyxel.btnp(pyxel.KEY_0):
			self.display = 1
		if pyxel.btnp(pyxel.KEY_R):
			for p1 in range(8):
				for p2 in range(8):
					if p1 != p2:
						self.rules[(p1+1,p2+1)]=ran(-10,10)/7
		if pyxel.btnp(pyxel.KEY_F):
			self.rules = {}
			for Y in range(8):
					self.rules[(Y+1,Y+1)]=1
					self.rules[(Y+2,Y+1)]=1
	def draw(self):
		pyxel.cls(0)
		pyxel.mouse(True)
		#pyxel.circ((self.p[0][x]+self.p[1][x])/2,(self.p[0][y]+self.p[1][y])/2,10,7)
		for p in self.p:
			"""if p[x] > 599:
				p[v][x] = abs(p[v][x])*-1
			if p[y] > 599:
				p[v][y] = abs(p[v][y])*-1
			if p[x] < 0:
				p[v][x] = abs(p[v][x])
			if p[y] < 0:
				p[v][y] = abs(p[v][y])"""
			p[x] %= 600
			p[y] %= 600
			if not p[v][x] == 0:
				p[x] += p[v][x]
				p[v][x] = p[v][x]/1.1
			if not p[v][y] == 0:
				p[y] += p[v][y]
				p[v][y] = p[v][y]/1.1
			pyxel.circ(p[x],p[y],5,p[c])
			if self.display == 0:
				pyxel.text(0,0,'F-reset with "fish" self.rules\nR-random self.rules\n0-close text overlay',9)
			"""if p[c] == 1:
				p[v][x] += vector_between((pyxel.mouse_x,pyxel.mouse_y),(p[x],p[y]),dist((p[x],p[y]),(pyxel.mouse_x,pyxel.mouse_y)))[0]
				p[v][y] += vector_between((pyxel.mouse_x,pyxel.mouse_y),(p[x],p[y]),dist((p[x],p[y]),(pyxel.mouse_x,pyxel.mouse_y)))[1]"""
			for pp in self.p:
				self.dist = dist((p[x],p[y]),(pp[x],pp[y]))
				self.th = vector_between((pp[x],pp[y]),(p[x],p[y]),self.dist)
				if (p[c],pp[c]) in self.rules:
					p[v] = apply_actration(p[v],self.th,self.rules[(p[c],pp[c])],self.dist)
				else:
					p[v] = apply_actration(p[v],self.th,0,self.dist)
			

				
		

App()






"""import pyxel  
from math import *
from random import randint as ran
import random
def angle_between(a, b):
    angle = (atan2(a[1] - b[1], b[0] - a[0]))
    return radians(180-degrees(angle)) 

x= 0
y= 1
c= 2
f =[[0,0,1]]  
#random.seed(1)
for i in range(200):
            f.append([ran(0,599),ran(0,599),ran(1,8)])    
class App:
    def __init__(self):
        pyxel.init(600, 600,fps=60)
        pyxel.colors[1] = 0xff3333
        pyxel.colors[2] = 0xff8833
        pyxel.colors[3] = 0xffff33
        pyxel.colors[4] = 0x33ff33
        pyxel.colors[5] = 0x33ffff
        pyxel.colors[6] = 0x3333ff
        pyxel.colors[7] = 0xaa33ff
        pyxel.colors[8] = 0xff33ff   
        self.p = []
        for i in f:
             self.p.append(i)  
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT,repeat=10):
             self.p.append([pyxel.mouse_x,pyxel.mouse_y,ran(1,8)])
            
    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(True)
        for p in self.p:
            pyxel.circ(p[x],p[y],7,p[c])
            for pp in self.p:
                dis = dist([p[x],p[y]],[pp[x],pp[y]])
                if dis < 200:
                    if (p[c] == pp[c] or p[c] == (pp[c])+1):
                    #if p[c] == pp[c] :
                        if dis < 100 and dis > 50:
                            p[x] -= cos(angle_between([p[x],p[y]],[pp[x],pp[y]]))/1
                            p[y] -= sin(angle_between([p[x],p[y]],[pp[x],pp[y]]))/1
                        elif dis < 50 :
                            p[x] -= cos(angle_between([p[x],p[y]],[pp[x],pp[y]]))/2
                            p[y] -= sin(angle_between([p[x],p[y]],[pp[x],pp[y]]))/2
                    if dis < 20:
                        p[x] += cos(angle_between([p[x],p[y]],[pp[x],pp[y]]))*1 
                        p[y] += sin(angle_between([p[x],p[y]],[pp[x],pp[y]]))*1 


                p[x] = p[x]%600
                p[y] = p[y]%600
            

                
        

App()"""
