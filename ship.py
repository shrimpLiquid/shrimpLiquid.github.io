import pyxel    
from math import cos,sin,radians,dist,degrees,atan2,sqrt
def val(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
def angle_between(a, b):
    angle = degrees(atan2(a[1] - b[1], b[0] - a[0]))
    if angle < 0:
        angle += 360
    return radians(180-angle)
   
   
def point_inside_circle(px, py, cx, cy, r):
    return (px - cx)**2 + (py - cy)**2 <= r**2
   
def triangle_circle_intersection(t_vertices, cx, cy, r):
        (x1, y1), (x2, y2), (x3, y3) = t_vertices
        if (point_inside_circle(x1, y1, cx, cy, r) or
            point_inside_circle(x2, y2, cx, cy, r) or
            point_inside_circle(x3, y3, cx, cy, r)):
            return True
        return False
   
   
   
x=0
y=1
r=2
s=3
stars = []
for i in range(pyxel.rndi(7,20)):
    stars.append((pyxel.rndi(0,200),pyxel.rndi(20,220),pyxel.rndi(0,1)))
class App:
    def __init__(self):
        self.p = [[10,90,0,0,0]]
        self.t = [100,100]
        self.d = 100
        self.s = 0
        self.txt = True
        self.size=10
        self.stars = stars
        pyxel.init(200,220)
        pyxel.colors[4] = 0x306699
        pyxel.colors[1] = 0xee3333
        pyxel.colors[2] = 0xff4444
        pyxel.colors[13] = 0x882233
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
            self.stars = []
            for i in range(pyxel.rndi(7,20)):
                self.stars.append((pyxel.rndi(0,200),pyxel.rndi(20,220),pyxel.rndi(0,1)))
        pyxel.cls(0)
       
        for S in self.stars:
            pyxel.circ(S[x],S[y],S[r],8)
        pyxel.circ(self.t[x],self.t[y],self.size,1)
        pyxel.circb(self.t[x],self.t[y],self.size,13)
        for p in self.p:
#             pyxel.camera(p[x]-100,p[y]-100)
            """if p[r]  < angle_between(self.t,p):
                p[r]+= 0.15
            if p[r]  > angle_between(self.t,p):
                p[r]-= 0.15"""
            # if dist((self.t[x],self.t[y]),(p[x],p[y])) < self.size+4:
            if triangle_circle_intersection(((p[x]+cos(p[r])*5,p[y]+sin(p[r])*5),(p[x]+cos(p[r]+radians(180-30))*5,p[y]+sin(p[r]+radians(180-30))*5),(p[x]+cos(p[r]-radians(180-30))*5,p[y]+sin(p[r]-radians(180-30))*5)),self.t[x],self.t[y],self.size):
                self.d = 100
                self.s += 1
                if self.s%10==0:
                    self.size -= 0.5
                self.t[x],self.t[y] = pyxel.rndi(0,200),pyxel.rndi(20,220)
            if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y))  and self.d > 0:
                self.d-=1
                self.txt = 0
                pyxel.tri(p[x]+cos(p[r])*-8,p[y]+sin(p[r])*-8,p[x]+cos(p[r]+radians(180-30))*5,p[y]+sin(p[r]+radians(180-30))*5,p[x]+cos(p[r]-radians(180-30))*5,p[y]+sin(p[r]-radians(180-30))*5,7)
                if p[s] < 5:
                        p[s] += 0.1
            else:
                self.d-=0.5
                p[s] *= 0.95

            p[x] += cos(p[r])*(p[s])
            p[y] += sin(p[r])*(p[s])
            #pyxel.circ(p[x],p[y],2,4)
            pyxel.tri(p[x]+cos(p[r])*5,p[y]+sin(p[r])*5,p[x]+cos(p[r]+radians(180-30))*5,p[y]+sin(p[r]+radians(180-30))*5,p[x]+cos(p[r]-radians(180-30))*5,p[y]+sin(p[r]-radians(180-30))*5,11)
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                p[r] +=-0.15 + val(p[s],0,5,0,0.05)
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                p[r] +=0.15 - val(p[s],0,5,0,0.05)
            if p[s] < 0:
                p[s] = 0
            if p[x] >199:
                p[r]=radians(180)-p[r]
                p[x] -= 5
            if p[x] <0:
                p[r]=radians(180)-p[r]
                p[x] += 5
            if p[y] >219:
                p[r]=radians(360)-p[r]
                p[y] -= 5
            if p[y] <20:
                p[r]=radians(360)-p[r]
                p[y] += 5

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