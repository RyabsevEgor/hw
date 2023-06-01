#🟩⬛🚁🌲🌳🔥🌊🏆☁️🌩️⚡🏥🏬🧯🧡
from map import Map
import time
import os


TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

tmp = Map(MAP_W, MAP_H)
tmp.generate_forest(4, 10)
tmp.generetae_river(30)
tmp.generetae_river(10)


tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()

tmp.print_map()



tick = 1

while True:
    os.system('cls')
    print('TICK', tick)
    tmp.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fires()
    