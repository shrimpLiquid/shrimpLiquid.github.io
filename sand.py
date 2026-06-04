import pyxel
from random import randint as ran
from math import trunc as cut
fall = [0,3,6]

waterfall = fall
waterfall.remove(3)

base = []
elements = {0:"air",
            10:"sand",
            3:"water",
            4:"wood",
            9:"fire",
            13:"metal",
            6:"steam"
            }
size = 100
yyyyy = []
for i in range(size):
    yyyyy.append(0)
for i in range(size):
    base.append(list(yyyyy))

class App:
    def __init__(self):
        self.e = 10
        self.grid = base
        self.bs = 0
        pyxel.init(size, size+5,fps=120)
        pyxel.screen_mode(1)
        pyxel.run(self.update, self.draw)


    def update(self):

        self.bs = abs(self.bs + pyxel.mouse_wheel)
       
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            X,Y = pyxel.mouse_x,pyxel.mouse_y
            for x in range((self.bs*2)+1):
                for y in range((self.bs*2)+1):
                    if (not self.e in [9]) or self.grid[pyxel.clamp((x-self.bs)+X,1,size-2)][pyxel.clamp((y-self.bs)+Y,2,size-2)] == 0:
                        self.grid[pyxel.clamp((x-self.bs)+X,1,size-2)][pyxel.clamp((y-self.bs)+Y,2,size-2)] = self.e
       
        if pyxel.btn(pyxel.KEY_0):
            self.e = 0
        if pyxel.btn(pyxel.KEY_1):
            self.e = 10
        if pyxel.btn(pyxel.KEY_2):
            self.e = 3
        if pyxel.btn(pyxel.KEY_3):
            self.e = 4
        if pyxel.btn(pyxel.KEY_4):
            self.e = 9
        if pyxel.btn(pyxel.KEY_5):
            self.e = 13
        if pyxel.btn(pyxel.KEY_6):
            self.e = 6
       

        for x in range(size):
            for y in range(size):
                #SAND
                if self.grid[x][y] == 10:
                    for i in range(3):
                        ofset = ((i+1)%3)-1
                        if self.grid[x+ofset][y+1] in fall and 0 < x+ofset < size-1 and y < size-2:
                            self.grid[x][y] = self.grid[x+ofset][y+1]
                            self.grid[x+ofset][y+1] = -10
                            break
                       
               #WATER
                if self.grid[x][y] == 3:
                    ofset = (pyxel.rndi(0,1)*2)-1
                    X = x
                    Y = y
                    if abs(self.grid[X+ofset][Y]) in waterfall and 0 < X+ofset < size-1:
                        X+=ofset
                    if abs(self.grid[X][Y+1]) in waterfall  and Y < size-2:
                        Y+=1
                   
                    if (X,Y) != (x,y):
                        self.grid[x][y] = self.grid[X][Y]
                        self.grid[X][Y] = -3

                    if cut(self.grid[X][Y+1]) < round(self.grid[X][Y+1],1):
                        self.grid[X][Y] = -6
                       
                #FIRE      
                if self.grid[x][y] == 9:
                    X = x
                    Y = y

                    for I in range(2):
                        i = (I*2)-1
                        if abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y]) == 4:
                            self.grid[X+i][Y] = -9
                    if abs(self.grid[X][pyxel.clamp(Y+1,1,size-2)]) == 4:
                        self.grid[X][Y+1] = -9

                    ofset = (pyxel.rndi(0,1)*2)-1
                    if self.grid[X+ofset][Y] in [4,0,9] and 0 < X+ofset < size-1:
                        X+=ofset
                    if self.grid[X][Y-1] in [4,0,9]:
                        Y -= 1
                    if Y-1 < 1:
                        self.grid[x][y] = 0
                    elif (X,Y) != (x,y):
                        self.grid[x][y] = 0
                        self.grid[X][Y] = -9
                       
                       
                #metal
                if cut(self.grid[x][y]) == 13:
                    mciq = round(self.grid[x][y],1)
                    if mciq > 13.0 and pyxel.rndi(0,10) == 0:
                        self.grid[x][y] -= 0.1
                    if self.grid[x][y+1] == 9:
                        self.grid[x][y] = 13.9
                        self.grid[x][y+1] = 0
                    if cut(self.grid[x][y+1]) == 13 and self.grid[x][y+1]:
                        self.grid[x][y] = self.grid[x][y+1]

                #steam
                if self.grid[x][y] == 6:
                    if pyxel.rndi(0,1000) == 0:
                        self.grid[x][y] = -3
                        break
                    X = x
                    Y = y
                    ofset = (pyxel.rndi(0,1)*2)-1
                    if self.grid[X+ofset][Y] in [3,0] and 0 < X+ofset < size-1:
                        X+=ofset
                    if self.grid[X][Y-1] in [3,0]:
                        Y -= 1
                    if Y-1 < 1:
                        Y+=1
                    elif (X,Y) != (x,y):
                        self.grid[x][y] = 0
                        self.grid[X][Y] = -6       

                   
                   
        for x in range(size):
            for y in range(size):
                self.grid[x][y] = abs(self.grid[x][y])
                if y > size-2:
                    self.grid[x][y] = 0 
                   

    def draw(self):
        pyxel.cls(0)
        pyxel.camera(0,-5)
        for x in range(size):
            for y in range(size):
                pyxel.pset(x,y,cut(self.grid[x][y]))
                # if cut(self.grid[x][y]) < round(self.grid[x][y],1):
                #     pyxel.pset(x,y,8)
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,cut(7))
        pyxel.text(0,-5,str(self.bs+1),7)
        pyxel.text(10,-5,str(elements[cut(self.e)]),cut(self.e))
        # pyxel.text(1,1,str(self.bs+1),7)

App()