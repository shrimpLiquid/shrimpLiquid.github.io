import pyxel
from random import randint as ran
fall = [0,3]

base = []
elements = {0:"air",
            10:"sand",
            3:"water",
            4:"wood",
            9:"fire"
            }
size = 100
yyyyy = []
for i in range(size):
    yyyyy.append(0)
for i in range(size):
    base.append(list(yyyyy))
global element
class App:
    def __init__(self):
        self.e = 10
        self.grid = base
        self.bs = 0
        def element(pX,pY):
            return self.grid[pX][pY]
        pyxel.init(size, size+5,fps=120)
        pyxel.screen_mode(1)
        pyxel.run(self.update, self.draw)


    def update(self):
        try:
            element(0,0)
        except:
            def element(pX,pY):
                return self.grid[pX][pY]
        self.bs = abs(self.bs + pyxel.mouse_wheel)
       
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            X,Y = pyxel.mouse_x,pyxel.mouse_y
            for x in range((self.bs*2)+1):
                for y in range((self.bs*2)+1):
                    if (not self.e in [9]) or element(pyxel.clamp((x-self.bs)+X,1,size-2),pyxel.clamp((y-self.bs)+Y,2,size-2)) == 0:
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
       

        for x in range(size):
            for y in range(size):
                #SAND
                if element(x,y) == 10:
                    for i in range(3):
                        ofset = ((i+1)%3)-1
                        if element(x+ofset,y+1) in fall and 0 < x+ofset < size-1 and y < size-2:
                            self.grid[x][y] = element(x+ofset,y+1)
                            self.grid[x+ofset][y+1] = -10
                            break
                       
               #WATER
                if element(x,y) == 3:
                    ofset = (pyxel.rndi(0,1)*2)-1
                    X = x
                    Y = y
                    if element(X+ofset,Y) == 0 and 0 < X+ofset < size-1:
                        X+=ofset
                    if element(X,Y+1) == 0  and Y < size-2:
                        Y+=1
                   
                    if (X,Y) != (x,y):
                        self.grid[x][y] = 0
                        self.grid[X][Y] = -3
                       
                #FIRE      
                if element(x,y) == 9:
                    X = x
                    Y = y

                    for I in range(2):
                        i = (I*2)-1
                        if abs(element(pyxel.clamp(X+i,1,size-1),Y)) == 4:
                            self.grid[X+i][Y] = -9
                    if abs(element(X,pyxel.clamp(Y+1,1,size-2))) == 4:
                        self.grid[X][Y+1] = -9

                    ofset = (pyxel.rndi(0,1)*2)-1
                    if element(X+ofset,Y) in [4,0,9] and 0 < X+ofset < size-1:
                        X+=ofset
                    if element(X,Y-1) in [4,0,9]:
                        Y -= 1
                    if Y-1 < 1:
                        self.grid[x][y] = 0
                    elif (X,Y) != (x,y):
                        self.grid[x][y] = 0
                        self.grid[X][Y] = -9
                       
                       
                #cold metal
                if self.grid[x][y] == 13:
                    pass
                   
                   
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
                pyxel.pset(x,y,self.grid[x][y])
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,7)
        pyxel.text(0,-5,str(self.bs+1),7)
        pyxel.text(10,-5,str(elements[self.e]),self.e)
        # pyxel.text(1,1,str(self.bs+1),7)

App()