import pyxel    
from math import cos,sin,radians,dist,degrees,atan2
def val(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
def angle_between(a, b):
    angle = degrees(atan2(a[1] - b[1], b[0] - a[0]))
    if angle < 0:
        angle += 360
    return radians(180-angle)
x=0
y=1
r=2
s=3
stars = []
for i in range(10):
    stars.append((pyxel.rndi(0,200),pyxel.rndi(20,220),pyxel.rndi(0,1)))
class App:
    def __init__(self):
        self.p = [[10,90,0,[0,0],0]]
        self.t = [100,100]
        self.d = 100
        self.s = 0
        self.txt = True
        self.size=10
        pyxel.init(200,220)
        pyxel.colors[4] = 0x306699
        pyxel.colors[1] = 0xee3333
        pyxel.colors[2] = 0xff4444
        pyxel.colors[3] = 0x111111
        pyxel.colors[5] = 0xffff00
        pyxel.colors[6] = 0xffCC00
        pyxel.colors[7] = 0xff9900
        pyxel.colors[8] = 0xffffff
        pyxel.colors[11] = 0x4d6783
        pyxel.colors[12] = 0x2d3743
        pyxel.run(self.update, self.draw)
    def update(self):
        pass

        
    def draw(self):
        if pyxel.btnp(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.p = [[10,90,0,0,0]]
            self.t = [100,100]
            self.d = 100
            self.s = 0
            self.txt = True
            self.size=10
        pyxel.cls(0)
        for S in stars:
            pyxel.circ(S[x],S[y],S[r],8)
        pyxel.circ(self.t[x],self.t[y],self.size,1)
        for p in self.p:
            """if p[r]  < angle_between(self.t,p):
                p[r]+= 0.15
            if p[r]  > angle_between(self.t,p):
                p[r]-= 0.15"""
            if dist((self.t[x],self.t[y]),(p[x],p[y])) < self.size+4:
                self.d = 100
                self.s += 1
                if self.s%10==0:
                    self.size -= 0.5
                self.t[x],self.t[y] = pyxel.rndi(0,200),pyxel.rndi(20,220)
            if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y))  and self.d > 0:
                self.d-=1
                self.txt = 0
                pyxel.tri(p[x]+cos(p[r])*-8,p[y]+sin(p[r])*-8,p[x]+cos(p[r]+radians(180-30))*5,p[y]+sin(p[r]+radians(180-30))*5,p[x]+cos(p[r]-radians(180-30))*5,p[y]+sin(p[r]-radians(180-30))*5,7)
                if p[s][x] < 5:
                        p[s][x] += 0.1*cos(p[r])
                if p[s][y] < 5:
                        p[s][y] += 0.1*sin(p[r])
            else:
                self.d-=0.5
                for iii in range(2):
                    if p[s][iii] > 0.0:
                        p[s][iii] -= 0.1
                    if p[s][iii] < 0:
                        p[s][iii] = 0
            p[x] += p[s][x]
            p[y] += p[s][y]
            #pyxel.circ(p[x],p[y],2,4)
            pyxel.tri(p[x]+cos(p[r])*5,p[y]+sin(p[r])*5,p[x]+cos(p[r]+radians(180-30))*5,p[y]+sin(p[r]+radians(180-30))*5,p[x]+cos(p[r]-radians(180-30))*5,p[y]+sin(p[r]-radians(180-30))*5,11)
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                p[r] +=-0.15
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                p[r] +=0.15
            

            """pyxel.circ(185,15,7,5)
            pyxel.line(185,15,185+ cos(p[r])*5,15+ sin(p[r])*5,1)
            pyxel.circ(15,15,9,5)
            pyxel.line(15,15,15+ cos(val(p[s],0,4,-3.1416,0))*7,15+ sin(val(p[s],0,4,-3.1416,0))*7,1)"""
            pyxel.rect(0,0,200,20,11)
            pyxel.rect(50,5,100,10,0)
            pyxel.rectb(1,1,200-2,20-2,12)
            pyxel.dither(0.5)
            pyxel.rect(50,5,100,10,12)
            pyxel.dither(1)
            pyxel.rect(50,5,self.d,10,5)
            pyxel.dither((100-self.d)/100)
            pyxel.rect(50,5,self.d,10,7)
            pyxel.dither(1)
            pyxel.text(20,8,str(self.s),7)
            if self.txt:
                pyxel.text(17,18,"use arrow keys to move. use R to restart.",7)
App()