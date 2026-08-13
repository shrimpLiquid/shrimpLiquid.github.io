import pyxel
from random import randint as ran
from math import trunc
fall = [0,3,6,15,19,20,9,109]

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

burn = [21,4,15]

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
            20:"smoke",
            21:"gunpowder",
            22:"lava",
            }

elearry = []
for e in elements:
    if e not in [20]:
        elearry.append(e)

explosionsize = 10

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
        self.ball = True
        pyxel.colors[14] = 0xA09595
        pyxel.colors[12] = 0x505050
        pyxel.colors[15] = 0xbc8c03
        pyxel.colors[8] = 0xffaa000
        pyxel.colors.append(0xcc8c00)
        pyxel.colors.append(0x6b4852)
        pyxel.colors.append(0xdddddd)
        pyxel.colors.append(0xaaff00)
        pyxel.colors.append(0x252525)
        pyxel.colors.append(0x795F4D)
        pyxel.colors.append(0xdf3a3f)
        pyxel.init(size+5, size+5,fps=60)
        pyxel.screen_mode(1)
        pyxel.run(self.update, self.draw)


    def update(self):
        self.bs = max(self.bs + int(pyxel.mouse_wheel/1),0)

        for s in self.spouts:
           self.grid[s[0]][s[1]] = s[2]

        if not pyxel.btn(pyxel.KEY_SHIFT):
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x-5 > 0 and pyxel.mouse_y-5 > 1:
                X,Y = pyxel.mouse_x-5,pyxel.mouse_y-5
                
                pyxel.circ(X-5,Y,self.bs/2,1)
                for x in range((self.bs)+1):
                    for y in range((self.bs)+1):
                        if ((not self.e in [9]) or self.grid[pyxel.clamp((x-int(self.bs/2))+X,1,size-2)][pyxel.clamp((y-int(self.bs/2))+Y,2,size-2)] == 0) and (pyxel.pget(pyxel.clamp((x-int(self.bs/2))+X,1,size-2),pyxel.clamp((y-int(self.bs/2))+5+Y,2,size-2)) == 1 or not self.ball):
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
        if pyxel.btnp(pyxel.KEY_COMMA):
            self.ball = not self.ball
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
            self.e = 21
        if pyxel.btn(pyxel.KEY_E):
            self.e = 22

        xs = range(size) if pyxel.frame_count % 2 == 0 else range(size - 1, -1, -1)
        for x in xs:
            for y in range(size - 1, -1, -1):
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
                        dir = ((x%2)*2)-1
                        if self.grid[x+dir][y]:
                            dir*=-1
                        X = x
                        Y = y
                        for I in range(10):
                            ofset = (I+1)*(dir)
                            if 0 < X+ofset < size-1 and abs(self.grid[X+ofset][Y]) in waterfall and self.grid[X][Y+1]:
                                X+=dir
                            else:
                                break
                        if abs(self.grid[X][Y+1]) in waterfall  and Y < size-2:
                            Y+=1
   
                        if (X,Y) != (x,y):
                            self.grid[x][y] = self.grid[X][Y]
                            self.grid[X][Y] = -3

                        if Y + 1 < size and self.grid[X][Y + 1] == 14:
                            self.grid[X][Y] = -6
   
                    #FIRE
                    elif pix == 9:
                        X = x
                        Y = y
                        for I in range(2):
                            i = (I*2)-1
                            if abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y]) == 4:
                                self.grid[X+i][Y] = -17
                            if abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y]) == 15:
                                self.grid[X+i][Y] = -9
                            if abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y]) == 21:
                                self.grid[X+i][Y] = 121
                        for I in range(2):
                            i = (I*2)-1
                            if abs(self.grid[X][pyxel.clamp(Y+i,1,size-2)]) == 4:
                                self.grid[X][Y+i] = -17
                            if abs(self.grid[X][pyxel.clamp(Y+i,1,size-2)]) == 15:
                                self.grid[X][Y+i] = -9
                            if abs(self.grid[X][pyxel.clamp(Y+i,1,size-2)]) == 21:
                                self.grid[X][Y+i] = 121
   
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
                            self.grid[X][Y] = -pix
   
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
                        dir = (pyxel.rndi(0,1)*2)-1
                        if self.grid[x+dir][y]:
                            dir*=-1
                        X = x
                        Y = y
                        for I in range(10):
                            ofset = (I+1)*(dir)
                            if 0 < X+ofset < size-1 and abs(self.grid[X+ofset][Y]) in oilfall and self.grid[X][Y+1]:
                                X+=dir
                            else:
                                break
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
                    
                    #gunpowder
                    elif pix == 21:
                        for i in range(3):
                            ofset = ((i+1)%3)-1
                            if (self.grid[x+ofset][y+1] in fall) and 0 < x+ofset < size-1 and y < size-2:
                                self.grid[x][y] = self.grid[x+ofset][y+1]
                                self.grid[x+ofset][y+1] =pix*-1
                                break
                    elif pix == 121 and pyxel.rndi(0,10) == 0:
                        for xr in range((explosionsize)+1):
                            for yr in range((explosionsize)+1):
                                XX,YY = pyxel.clamp((xr-int(explosionsize/2))+x,1,size-2),pyxel.clamp((yr-int(explosionsize/2))+y,2,size-2)
                                self.grid[XX][YY] = -9
                    
                    #LAVA
                    elif pix == 22:
                        X = x
                        Y = y
                        for I in range(2):
                            i = (I*2)-1
                            place = abs(self.grid[pyxel.clamp(X+i,1,size-1)][Y])
                            if place == 3:
                                self.grid[X][Y] = 12
                                if pyxel.rndi(0,10) == 0:
                                    self.grid[X+i][Y] = -6
                            if place in burn:
                                self.grid[X+i][Y] = 9
                        for I in range(2):
                            i = (I*2)-1
                            place = abs(self.grid[X][pyxel.clamp(Y+i,1,size-2)])
                            if place == 3:
                                self.grid[X][Y] = 12
                                if pyxel.rndi(0,10) == 0:
                                    self.grid[X][Y+i] = 6
                            if place in burn:
                                self.grid[X][Y+i] = 9
                            ofset = (pyxel.rndi(0,1)*2)-1
                            if abs(self.grid[X+ofset][Y]) in goopfall and 0 < X+ofset < size-1:
                                X+=ofset
                        if abs(self.grid[X][Y+1]) in goopfall  and Y < size-2:
                            Y += 1
   
                        if (X,Y) != (x,y):
                            self.grid[x][y] = self.grid[X][Y]
                            self.grid[X][Y] = -22
                                        
                


    def draw(self):
        pyxel.cls(0)
        pyxel.camera(-5,-5)
        for x in range(size):
            for y in range(size):
                pix = self.grid[x][y]
                if y > size-2:
                    self.grid[x][y] = 0
                elif pix != 0:
                    self.grid[x][y] = abs(pix)
                    pyxel.pset(x,y+1,(self.grid[x][y])%100)

        pyxel.circ(95,-2,3,7)
        pyxel.line(93,-2,97,-2,3)
        pyxel.line(95,0,95,-4,3)

        pyxel.circ(85,-2,3,7)
        pyxel.line(83,-2,87,-2,22)

        pyxel.circ(75,-2,3,7)
        pyxel.line(74,-1,76,-3,4)

        if self.ball:
            pyxel.circb(65,-2,2,7)
        else:
            pyxel.rectb(63,-4,5,5,7)


        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_y-5 < 1:
            if 95+3 > pyxel.mouse_x-5 > 95-3:
                self.bs+=1
            if 85+3 > pyxel.mouse_x-5 > 85-3:
                self.bs-=1
            if 75+3 > pyxel.mouse_x-5 > 75-3:
                pyxel.screen_mode(self.smooth)
                self.smooth = not self.smooth
            if 65+2 > pyxel.mouse_x-5 > 65-2:
                self.ball = not self.ball
            

        for i in range(len(elearry)):
            pyxel.rect(-5,i*6,6,5,elearry[i])
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                if pyxel.mouse_x-5 < 0:
                    if (i*6)+6 > pyxel.mouse_y-5 > (i*6):
                        self.e = elearry[i]
        pyxel.pset(pyxel.mouse_x-5,pyxel.mouse_y-4,7)
        pyxel.line(0,1,0,100,7)
        pyxel.line(1,2,100,2,7)
        pyxel.text(0,-5,str(self.bs+1),7)
        pyxel.text(10,-5,str(elements[self.e]),self.e%100)
        if self.e in dark:
            pyxel.text(10,-5,str(elements[self.e]),7)

        # pyxel.text(1,1,str(self.bs+1),7)

App()