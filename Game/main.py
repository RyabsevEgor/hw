#🟩⬛🚁🌲🌳🔥🌊🏆☁️⚡🏥🏬🧯🧡
from clouds import Clouds
from map import Map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 30
CLOUDS_UPDATE = 300
MAP_W, MAP_H = 20, 10

tmp = Map(MAP_W, MAP_H)
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
clouds = Clouds(MAP_W, MAP_H)
clouds.update_clouds()

helico = Helico(MAP_W, MAP_H)


MOVES = {'w': (-1, 0), 'd' : (0, 1), 's' : (1, 0), 'a' : (0,-1)}
def process_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helico.move(dx,dy)

    #if key == keyboard.Key.esc:
    #    # Stop listener
    #    return False

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()






tick = 1

while True:
    os.system('cls')
    tmp.process_helicopter(helico, clouds)
    helico.print_stats()
    tmp.print_map(helico, clouds)
    print('TICK', tick,)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update_clouds()