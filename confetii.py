import pyxel
from math import *
from time import time
def angle_points(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return (atan2(dy, dx))

distance = 50

class App:
    def __init__(self):
        pyxel.init(200,200,fps=60)
        self.p=[]
        self.pt=0
        self.dt=0
        self.stance = 0
        pyxel.screen_mode(1)
        pyxel.colors.from_list([0x0,0xff0000,0xff8800,0xffff00,0x88ff00,0x00ff00,0x00ff88,0x00ffff,0x0088ff,0x0000ff,0x8800ff,0xff00ff,0xff0088,0xffffff])
        pyxel.run(self.update, self.draw)

    def update(self):
        #DONT MESS WITH THIS
        self.dt = (time() - self.pt)*10
        self.pt = time()
        #THIS
       
        for p in self.p:
            if min(max(0,p[1]),pyxel.width) != p[1] or min(max(0,p[0]),pyxel.height) != p[0]:
                self.p.remove(p)
            p[0] += p[2][0]*self.dt
            p[1] += p[2][1]*self.dt
            p[2][1] += self.dt/2
            p[2][0] *=  1-(self.dt/100)
            p[2][1] *=  1-(self.dt/100)
           
            if pyxel.btn(pyxel.KEY_SPACE):
                self.stance = (p[0]-pyxel.mouse_x)**2 + (p[1]-pyxel.mouse_y)**2
                if self.stance < distance**2:
                    st = (distance-sqrt(self.stance))/20
                    p[2][1] -= sin(angle_points((p[0],p[1]),(pyxel.mouse_x,pyxel.mouse_y)))*st*self.dt
                    p[2][0] -= cos(angle_points((p[0],p[1]),(pyxel.mouse_x,pyxel.mouse_y)))*st*self.dt
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            for i in range(int(50*self.dt)):
                angle = radians(pyxel.rndi(0,360))
                st = pyxel.rndi(0,200)/80
               
                self.p.append([pyxel.mouse_x,pyxel.mouse_y,[cos(angle)*st,sin(angle)*st],pyxel.rndi(1,12),(max(0,pyxel.rndi(-5,2))+1)])
        if pyxel.btn(pyxel.KEY_M) or pyxel.btn(pyxel.KEY_Z):
            for i in range(int(100*self.dt)):
                angle = radians(pyxel.rndi(0,180))
                st = pyxel.rndi(0,200)/80
               
                self.p.append([100,0,[cos(angle)*st,sin(angle)*st],pyxel.rndi(1,12),(max(0,pyxel.rndi(-5,2))+1)])
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_L):
            for X in range(20):
                for i in range(int(max(pyxel.rndi(0,int(self.dt*5)),1))):
                    angle = radians(pyxel.rndi(0,180))
                    st = pyxel.rndi(0,200)/80
                   
                    self.p.append([X*10,0,[cos(angle)*st,sin(angle)*st],pyxel.rndi(1,12),(max(0,pyxel.rndi(-5,2))+1)])

    def draw(self):
        pyxel.cls(0)
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,13)
        pyxel.text(0,0,str(len(self.p)),9)
        for p in self.p:
            if p[4] == 2:
                if int(p[1]/4) % 2 == 0:    
                    pyxel.line(p[0]-2,p[1]-1,p[0],p[1]+1,p[3])
                    pyxel.line(p[0],p[1]+1,p[0]-2,p[1]+3,p[3])
                else:
                    pyxel.line(p[0],p[1]-1,p[0]-2,p[1]+1,p[3])
                    pyxel.line(p[0]-2,p[1]+1,p[0],p[1]+3,p[3])
            else:
                pyxel.circ(p[0],p[1],p[4]-2,p[3])
       


App()