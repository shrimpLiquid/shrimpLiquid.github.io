import pyxel
from random import randint as ran
fall = [0,3,6,15,19]

waterfall = list(fall)
waterfall.remove(3)
waterfall.append(2)
goopfall = list(fall)
oilfall = list(fall)
oilfall.remove(15)
oilfall.remove(3)
grapefall = list(fall)
grapefall.remove(3)

base = []

dark = [0,20]
elements = {0:"air",
            10:"sand",
            3:"water",
            4:"wood",
            9:"fire",
            13:"metal",
            11:"goop",
            12:"stone",
            15:"oil",
            2:"grapes",
            19:"acid",
            20:"smoke"
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
for i in range(size):
    base[i][size-1] = 5000

class App:
    def __init__(self):
        self.e = 10
        self.grid = base
        self.spouts = []
        self.bs = 0
        self.smooth = False
        pyxel.colors[14] = 0xA09595
        pyxel.colors[12] = 0x505050
        pyxel.colors[15] = 0xbc8c03
        pyxel.colors[8] = 0xffaa000
        pyxel.colors.append(0xcc8c00)
        pyxel.colors.append(0x6b4852)
        pyxel.colors.append(0xdddddd)
        pyxel.colors.append(0xaaff00)
        pyxel.colors.append(0x252525)
        pyxel.init(size, size+5,fps=60)
        pyxel.screen_mode(1)
        pyxel.run(self.update, self.draw)


    def update(self):

        self.bs = max(self.bs + int(pyxel.mouse_wheel/1),0)

        for s in self.spouts:
           self.grid[s[0]][s[1]] = s[2]

        if not pyxel.btn(pyxel.KEY_SHIFT):
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                X,Y = pyxel.mouse_x,pyxel.mouse_y
                for x in range((self.bs)+1):
                    for y in range((self.bs)+1):
                        if (not self.e in [9]) or self.grid[pyxel.clamp((x-int(self.bs/2))+X,1,size-2)][pyxel.clamp((y-int(self.bs/2))+Y,2,size-2)] == 0:
                            self.grid[pyxel.clamp((x-int(self.bs/2))+X,1,size-2)][pyxel.clamp((y-int(self.bs/2))+Y,2,size-2)] = self.e
        else:
           if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
               t = 1
               for s in self.spouts:
                   if (s[0],s[1]) == (pyxel.mouse_x,pyxel.mouse_y):
                       t = 0
               if t:
                self.spouts.append([pyxel.mouse_x,pyxel.mouse_y,self.e])
        if pyxel.btnp(pyxel.KEY_PERIOD):
            pyxel.screen_mode(self.smooth)
            self.smooth = not self.smooth
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
        if pyxel.btn(pyxel.KEY_Q):
            self.e = 19
        if pyxel.btn(pyxel.KEY_W):
            self.e = 20


        for x in range(size):
            for y in range(size):
                #SAND
                pix = self.grid[x][y]
                if pix != 0:
                    if pix == 10:
                        for i in range(3):
                            ofset = ((i+1)%3)-1
                            if (self.grid[x+ofset][y+1] in fall) and 0 < x+ofset < size-1 and y < size-2:
                                self.grid[x][y] = self.grid[x+ofset][y+1]
                                self.grid[x+ofset][y+1] = -10
                                break
                        if self.grid[x][y+1] in [8,14]:
                                self.grid[x][y] = -8
   
                   #WATER
                    elif pix == 3:
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
                    elif pix ==  9:
                        X = x
                        Y = y
   
                        for I in range(2):
                            i = (I*2)-1
                            if abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y]) == 4:
                                self.grid[X+i][Y] = -17
                            if abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y]) == 15:
                                self.grid[X+i][Y] = -9
                        for I in range(2):
                            i = (I*2)-1
                            if abs(self.grid[X][pyxel.clamp(Y+i,1,size-2)]) == 4:
                                self.grid[X][Y+i] = -17
                            if abs(self.grid[X][pyxel.clamp(Y+i,1,size-2)]) == 15:
                                self.grid[X][Y+i] = -9
   
                        ofset = (pyxel.rndi(0,1)*2)-1
                        if self.grid[X+ofset][Y] in [0,9] and 0 < X+ofset < size-1:
                            X+=ofset
                        if self.grid[X][Y-1] in [0,9]:
                            Y -= 1
                        else:
                            self.grid[x][y] = 0
                            break
                        if Y-1 < 1:
                            self.grid[x][y] = 0
                        elif (X,Y) != (x,y):
                            self.grid[x][y] = 0
                            self.grid[X][Y] = -9
   
                    #wood
                    elif pix ==  17 and pyxel.rndi(0,10) == 0:
                        self.grid[x][y] = -9
                        if self.grid[x][y-1] == 0:
                            self.grid[x][y-1] = -20
   
                    #metal
                    elif pix ==  13:
                        if self.grid[x][y+1] in [9,14]:
                            self.grid[x][y] = -14
                            if self.grid[x][y+1] == 9:
                                self.grid[x][y+1] = 0
                    elif pix ==  14:
                        if pyxel.rndi(0,2) == 0:
                            self.grid[x][y] = 13
   
   
   
                    #steam
                    elif pix ==  6:
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
                    if self.grid[x][y] == 15:
                        ofset = (pyxel.rndi(0,1)*2)-1
                        X = x
                        Y = y
                        if abs(self.grid[X+ofset][Y]) in oilfall and 0 < X+ofset < size-1:
                            X+=ofset
                        if abs(self.grid[X][Y+1]) in oilfall  and Y < size-2:
                            Y+=1
   
                        if (X,Y) != (x,y):
                            self.grid[x][y] = self.grid[X][Y]
                            self.grid[X][Y] = -15

                    #stone
                    elif pix ==  12:
                        if self.grid[x][y+1] in fall and y < size-2:
                            self.grid[x][y] = self.grid[x][y+1]
                            self.grid[x][y+1] = -12


                    #goop
                    elif pix ==  11:
                        X = x
                        Y = y
                        if pyxel.rndi(0,10) == 0:
                            ofset = (pyxel.rndi(0,1)*2)-1
                            if abs(self.grid[X+ofset][Y]) in goopfall and 0 < X+ofset < size-1:
                                X+=ofset
                        if pyxel.rndi(0,4) == 0:
                            if abs(self.grid[X][Y+1]) in goopfall  and Y < size-2:
                                Y += 1
   
                        if (X,Y) != (x,y):
                            self.grid[x][y] = self.grid[X][Y]
                            self.grid[X][Y] = -11
   
                    #grapes
                    elif pix ==  2:
                        for i in range(3):
                            ofset = ((i+1)%3)-1
                            if (self.grid[x+ofset][y+1] in grapefall) and 0 < x+ofset < size-1 and y < size-2:
                                self.grid[x][y] = self.grid[x+ofset][y+1]
                                self.grid[x+ofset][y+1] = -2
                                break
   
                    #glass
                    elif pix ==  8:
                        if pyxel.rndi(0,5) == 0 and not self.grid[x][y+1] in [8,0]:
                            self.grid[x][y] = -18
                            break
                        ofset = (pyxel.rndi(0,1)*2)-1
                        X = x
                        Y = y
                        if abs(self.grid[X+ofset][Y]) in fall and 0 < X+ofset < size-1:
                            X+=ofset
                        if abs(self.grid[X][Y+1]) in fall  and Y < size-2:
                            Y+=1
   
                        if (X,Y) != (x,y):
                            self.grid[x][y] = self.grid[X][Y]
                            self.grid[X][Y] = -8
   
                    #acid
                    elif pix ==  19:
                        ofset = (pyxel.rndi(0,1)*2)-1
                        X = x
                        Y = y
                        if abs(self.grid[X+ofset][Y]) not in [18,19] and 0 < X+ofset < size-1:
                            X+=ofset
                        if abs(self.grid[X][Y+1]) not in [18,19]  and Y < size-2:
                            Y+=1
   
                        if (X,Y) != (x,y):
                            if self.grid[X][Y] == 0:
                                self.grid[x][y] = 0
                                self.grid[X][Y] = -19
                            else:
                                self.grid[x][y] = 0
                                self.grid[X][Y] = 0

                    # smoke
                    elif pix == 20:
                        X = x
                        Y = y
                        ofset = (pyxel.rndi(0,1)*2)-1
                        if self.grid[X+ofset][Y] == 0 and 0 < X+ofset < size-1:
                            X+=ofset
                        if self.grid[X][Y-1] == 0:
                            Y -= 1
                        if Y-1 < 1:
                            Y+=1
                        elif (X,Y) != (x,y):
                            self.grid[x][y] = 0
                            self.grid[X][Y] = -20


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
                pix = self.grid[x][y]
                if pix != 0:
                    pyxel.pset(x,y+1,(self.grid[x][y]))
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y+1,7)
        pyxel.text(0,-5,str(self.bs+1),7)
        if self.e in dark:
            pyxel.rect(9,-5,20,6,91)
        pyxel.text(10,-5,str(elements[self.e]),self.e)
        # pyxel.text(1,1,str(self.bs+1),7)

App()