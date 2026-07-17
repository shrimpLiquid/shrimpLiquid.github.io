import pyxel
from math import *
import requests
from time import time
url = 'http://192.168.1.78/submit'
class App:
    def __init__(self):
        pyxel.init(100,100,fps=60)
        self.scores={}
        x = requests.post(url, json = "list")
        self.scores = eval(x.text)
        print(self.scores)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,7)

        for i, user in enumerate(self.scores):
            pyxel.text(1,1+i*6,user+" : "+str(self.scores[user]),7)
        

App()