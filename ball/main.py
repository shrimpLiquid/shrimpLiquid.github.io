# /// script
# dependencies = [
#     "cffi",
#     "raylib"
# ]
# ///

import asyncio
from pyray import *
from math import cos, sin, radians as rad

def scale(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

x,y,v,r,color = 0,1,2,3,4


guys = [[500,800,[0,0],0,0]]


async def main():
    init_window(1280, 720, "soup")
    while not window_should_close():
        set_target_fps(60)
        begin_drawing()
        clear_background(WHITE)
        
        for g in guys:
            draw_rectangle(int(g[x]-30),int(g[y]-30),60,60,RED)

            if g[y] < 600:
                g[v][y] += 5
            else:
                g[v][y] = 0

            if is_key_down(KeyboardKey.KEY_A):
                g[v][x] += -5
            if is_key_down(KeyboardKey.KEY_D):
                g[v][x] += +5
            if is_key_pressed(KeyboardKey.KEY_W) and g[v][y] < 0.01:
                g[v][y] += -50

            g[x] += g[v][x]
            g[v][x] = g[v][x]/1.5
            g[y] += g[v][y]



        end_drawing()

        await asyncio.sleep(0)
    close_window()


asyncio.run(main())
