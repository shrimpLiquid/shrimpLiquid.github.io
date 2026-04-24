# /// script
# dependencies = [
#   "raylib",
# ]
# ///
import asyncio
from pyray import *

x,y,v,r,color = 0,1,2,3,4
guys = [[500,100,[0.0,0.0],0,BLUE]]
platforms = [[100,600,1240,700],[800,500,900,550]]
speed = 4
gravity = 1.5

async def main():
    init_window(1280, 720, "soup")
    set_target_fps(60)
    
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)

        for g in guys:
            if g[v][y] < 0:
                g[v][y] += gravity
            else:
                g[v][y] += gravity*2
            if is_key_down(KeyboardKey.KEY_A): g[v][x] -= speed
            if is_key_down(KeyboardKey.KEY_D): g[v][x] += speed
            
            g[x] += g[v][x]
            for p in platforms:
                rect = Rectangle(p[x], p[y], p[2]-p[x], p[3]-p[y])
                if check_collision_circle_rec(Vector2(g[x], g[y]), 30, rect):
                    if g[v][x] > 0: g[x] = p[x] - 30.1
                    elif g[v][x] < 0: g[x] = p[2] + 30.1
                    g[v][x] = 0

            g[y] += g[v][y]
            on_ground = False
            for p in platforms:
                rect = Rectangle(p[x], p[y], p[2]-p[x], p[3]-p[y])
                if check_collision_circle_rec(Vector2(g[x], g[y]), 30, rect):
                    if g[v][y] > 0:
                        g[y] = p[y] - 30.1
                        g[v][y] = 0
                        on_ground = True
                    elif g[v][y] < 0:
                        g[y] = p[3] + 30.1
                        g[v][y] = 0

            g[v][x] *= 0.75

            if is_key_pressed(KeyboardKey.KEY_W) and on_ground:
                g[v][y] = -25

            draw_circle(int(g[x]), int(g[y]), 30, g[color])

        for p in platforms:
            draw_rectangle(p[x], p[y], p[2]-p[x], p[3]-p[y], BLACK)

        end_drawing()
        await asyncio.sleep(0)

    close_window()

asyncio.run(main())
