import pyxel
from random import randint as ran
fall = [0,3,6,15]

waterfall = list(fall)
waterfall.remove(3)
goopfall = list(fall)
oilfall = list(fall)
oilfall.remove(15)
oilfall.remove(3)

base = []
elements = {0:"air",
            10:"sand",
            3:"water",
            4:"wood",
            9:"fire",
            13:"metal",
            11:"goop",
            12:"stone",
            15:"oil",
            2:"grapes"
            }
            
elearry = []   
for e in elements:
    elearry.append(e)

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
        pyxel.colors[14] = 0xA09595
        pyxel.colors[12] = 0x505050
        pyxel.colors[15] = 0xbc8c03
        pyxel.colors.append(0xcc8c00)
        pyxel.init(size, size+5,fps=60)
        pyxel.screen_mode(1)
        pyxel.run(self.update, self.draw)


    def update(self):

        self.bs = max(self.bs + int(pyxel.mouse_wheel/1),0)
       
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
            self.e = 11
        if pyxel.btn(pyxel.KEY_7):
            self.e = 12
        if pyxel.btn(pyxel.KEY_8):
            self.e = 15
        if pyxel.btn(pyxel.KEY_9):
            self.e = 2
       

        for x in range(size):
            for y in range(size):
                #SAND
                if self.grid[x][y] == 10:
                    for i in range(3):
                        ofset = ((i+1)%3)-1
                        if (self.grid[x+ofset][y+1] in fall) and 0 < x+ofset < size-1 and y < size-2:
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

                    if self.grid[X][Y+1] == 14:
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
                        if abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y]) == 15:
                            self.grid[X+i][Y] = -16
                    if abs(self.grid[X][pyxel.clamp(Y+1,1,size-2)]) == 15:
                        self.grid[X][Y+1] = -16

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
                if self.grid[x][y] == 13:
                    if self.grid[x][y+1] in [9,14]:
                        self.grid[x][y] = -14
                        if self.grid[x][y+1] == 9:
                            self.grid[x][y+1] = 0
                if self.grid[x][y] == 14:
                    if pyxel.rndi(0,2) == 0:
                        self.grid[x][y] = 13
                       
                   

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
               
                #oil
                if self.grid[x][y] in [15,16]:
                    maybe = False
                    if self.grid[x][y]==16:
                        maybe = True
                        if pyxel.rndi(0,1) == 0:
                            self.grid[x][y] = -9
                            break
                    ofset = (pyxel.rndi(0,1)*2)-1
                    X = x
                    Y = y
                    if abs(self.grid[X+ofset][Y]) in oilfall and 0 < X+ofset < size-1:
                        X+=ofset
                    if abs(self.grid[X][Y+1]) in oilfall  and Y < size-2:
                        Y+=1
                   
                    if (X,Y) != (x,y):
                        self.grid[x][y] = self.grid[X][Y]
                        self.grid[X][Y] = (15+maybe)*-1

                #goop
                if self.grid[x][y] == 11:
                    X = x
                    Y = y
                    if pyxel.rndi(0,10) == 0:
                        ofset = (pyxel.rndi(0,1)*2)-1
                        if abs(self.grid[X+ofset][Y]) in goopfall and 0 < X+ofset < size-1:
                            X+=ofset
                    if abs(self.grid[X][Y+1]) in goopfall  and Y < size-2:
                        Y+=1
                   
                    if (X,Y) != (x,y):
                        self.grid[x][y] = self.grid[X][Y]
                        self.grid[X][Y] = -11
                
                #stone
                if self.grid[x][y] == 12:
                    if self.grid[x][y+1] in fall and y < size-2:
                        self.grid[x][y] = self.grid[x][y+1]
                        self.grid[x][y+1] = -12
                    
                #grapes
                if self.grid[x][y] == 2:
                    for i in range(3):
                        ofset = ((i+1)%3)-1
                        if (self.grid[x+ofset][y+1] in fall) and 0 < x+ofset < size-1 and y < size-2:
                            self.grid[x][y] = self.grid[x+ofset][y+1]
                            self.grid[x+ofset][y+1] = -2
                            break
                    

                   
                   
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
                pyxel.pset(x,y,(self.grid[x][y]))
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,7)
        pyxel.text(0,-5,str(self.bs+1),7)
        pyxel.text(10,-5,str(elements[self.e]),self.e)
        # pyxel.text(1,1,str(self.bs+1),7)

App()
