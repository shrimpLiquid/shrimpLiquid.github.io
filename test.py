
import pyxel
from random import randint as ran
x = 0
y = 1
fall = [0,3,7]
def common(a, b):
    result = [i for i in a if i in b]
    return result
class App:
    def __init__(self):
        self.e = 10
        self.sand = [[1000,1000]]
        self.water = [[1000,1000]]
        self.fire = [[1000,1000]]
        self.wood = [[1000,1000]]
        self.stone = [[1000,1000]]
        self.steam = [[1000,1000]]
        self.ice = [[1000,1000]]
        pyxel.init(100, 100,fps=60)
        pyxel.run(self.update, self.draw)


    def update(self):
        pyxel.colors[8] = 0xff0000
        for p in self.sand:
            if pyxel.pget(p[x],p[y]+1) in fall:
                p[y] = p[y] + 1
            
            if pyxel.pget(p[x],p[y]+1) == 10 or 11:
                if pyxel.pget(p[x]+1,p[y]+1) in fall:
                    p[x] = p[x] + 1
                    p[y] = p[y] + 1
                if pyxel.pget(p[x]-1,p[y]+1) in fall:
                    p[x] = p[x] - 1
                    p[y] = p[y] + 1
        for p in self.water:
            if pyxel.pget(p[x],p[y]+1) == 3:
                if pyxel.pget(p[x]+1,p[y]+1) == 0:
                    p[x] = p[x] + 1
                    p[y] = p[y] + 1
                if pyxel.pget(p[x]-1,p[y]+1) == 0:
                    p[x] = p[x] - 1
                    p[y] = p[y] + 1
            if pyxel.pget(p[x],p[y]+1) == 0:
                p[y] = p[y] + 1
            if ran(0,1) == 1:
                if pyxel.pget(p[x]+1,p[y]) == 0:
                    p[x] = p[x] + 1
            else:
                if pyxel.pget(p[x]-1,p[y]) == 0:
                    p[x] = p[x] - 1
        for p in self.fire:
            if ran(0,10) == 10:
                self.fire.remove(p)
            p[y] = p[y] - 1
            if ran(0,1) == 1:
                if pyxel.pget(p[x]+1,p[y]) == 0:
                    p[x] = p[x] + 1
            else:
                if pyxel.pget(p[x]-1,p[y]) == 0:
                    p[x] = p[x] - 1
        for p in self.wood:
            if pyxel.pget(p[x] + 1, p[y]) == 9 or pyxel.pget(p[x] - 1, p[y]) == 9:
                self.wood.remove(p)
                self.fire.append(p)
        for p in self.stone:
            if pyxel.pget(p[x],p[y]+1) in fall:
                p[y] = p[y] + 1
        for p in self.ice:
            if pyxel.pget(p[x],p[y]+1) in fall :
                if not [p[x],p[y]] in self.water:
                    p[y] = p[y] + 1
            if pyxel.pget(p[x] + 1, p[y])==9 or pyxel.pget(p[x] - 1, p[y])==9 or pyxel.pget(p[x] , p[y]-1) ==9 or pyxel.pget(p[x] ==9, p[y]+1)==9:
                self.ice.remove(p)
                self.water.append(p)

                    

    def draw(self):
        pyxel.cls(0)
        for p in self.stone:
            pyxel.pset(p[x],p[y],13)
        for p in self.wood:
            pyxel.pset(p[x],p[y],4)
        for p in self.sand:
            pyxel.pset(p[x],p[y],10)
        for p in self.water:
            pyxel.pset(p[x],p[y],3)
        for p in self.ice:
            pyxel.pset(p[x],p[y],12)
        for p in self.fire:
            pyxel.pset(p[x],p[y],9)
        for p in common(self.sand,self.water):
            pyxel.pset(p[x],p[y],11)
        for p in common(self.stone,self.water):
            pyxel.pset(p[x],p[y],12)
        for p in common(self.water,self.wood):
            pyxel.pset(p[x],p[y],1)
        pyxel.rectb(0,0,100,100,2)

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
            if self.e == 10:
                self.sand.append([pyxel.mouse_x,pyxel.mouse_y])
            if self.e == 3:
                self.water.append([pyxel.mouse_x,pyxel.mouse_y])
            if self.e == 9:
                self.fire.append([pyxel.mouse_x,pyxel.mouse_y])
            if self.e == 4:
                self.wood.append([pyxel.mouse_x,pyxel.mouse_y])
                self.wood.append([pyxel.mouse_x,pyxel.mouse_y-1])
                self.wood.append([pyxel.mouse_x-1,pyxel.mouse_y])
                self.wood.append([pyxel.mouse_x,pyxel.mouse_y+1])
                self.wood.append([pyxel.mouse_x+1,pyxel.mouse_y])
            if self.e == 13:
                self.stone.append([pyxel.mouse_x,pyxel.mouse_y])
            if self.e == 12:
                self.ice.append([pyxel.mouse_x,pyxel.mouse_y])
        if pyxel.btnp(pyxel.KEY_1):
            self.e = 10
        if pyxel.btnp(pyxel.KEY_2):
            self.e = 3
        if pyxel.btnp(pyxel.KEY_3):
            self.e = 9
        if pyxel.btnp(pyxel.KEY_4):
            self.e = 4
        if pyxel.btnp(pyxel.KEY_5):
            self.e = 13
        if pyxel.btnp(pyxel.KEY_6):
            self.e = 12
        if pyxel.btnp(pyxel.KEY_7):
            self.e = 8
        
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,14)
App()