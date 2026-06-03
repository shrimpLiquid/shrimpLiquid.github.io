
import pyxel
from random import randint as ran
fall = [0,3]

base = []
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
        self.ncells = []
        pyxel.init(size, size,fps=120)
        pyxel.screen_mode(1)
        pyxel.run(self.update, self.draw)


    def update(self):

        self.ncells.clear()

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.grid[pyxel.clamp(pyxel.mouse_x,1,size-2)][pyxel.clamp(pyxel.mouse_y,2,size-2)] = self.e
        if pyxel.btn(pyxel.KEY_1):
            self.e = 10
        if pyxel.btn(pyxel.KEY_2):
            self.e = 3

        for x in range(size):
            for y in range(size):
                if self.grid[x][y] == 10:
                    for i in range(3):
                        ofset = ((i+1)%3)-1
                        if self.grid[x+ofset][y+1] in fall and 0 < x+ofset < size-1 and y < size-2:
                            self.grid[x][y] = self.grid[x+ofset][y+1]
                            self.grid[x+ofset][y+1] = -10
                            break
                if self.grid[x][y] == 3:
                    ofset = (pyxel.rndi(0,1)*2)-1
                    X = x
                    Y = y
                    if self.grid[X+ofset][Y] == 0 and 0 < X+ofset < size-1:
                        X+=ofset
                    if self.grid[X][Y+1] == 0  and Y < size-2:
                        Y+=1
                    
                    if (X,Y) != (x,y):
                        self.grid[x][y] = 0
                        self.grid[X][Y] = -3
        for x in range(size):
            for y in range(size):
                self.grid[x][y] = abs(self.grid[x][y])
                    

    def draw(self):
        pyxel.cls(0)
        for x in range(size):
            for y in range(size):
                pyxel.pset(x,y,self.grid[x][y])
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,7)

App()