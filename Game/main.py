#🟩⬛🚁🌲🌳🔥🌊🏆☁️⚡🏥🏬🧯🧡
from clouds import Clouds
from map import Map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard
import json

TICK_SLEEP = 0.01
TREE_UPDATE = 400
FIRE_UPDATE = 600
CLOUDS_UPDATE = 500
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.add_fire()
field.add_fire()
field.add_fire()
field.add_fire()
field.add_fire()
clouds = Clouds(MAP_W, MAP_H)
clouds.update_clouds()

helico = Helico(MAP_W, MAP_H)


MOVES = {'w': (-1, 0), 'd' : (0, 1), 's' : (1, 0), 'a' : (0,-1)}
# F - сохранение G - восстановление
def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helico.move(dx,dy)
    elif c == 'f':
        data = {'helicopter': helico.export_data(),
                    'clouds': clouds.export_data(),
                     'field': field.export_data(),
                    'tick' : tick}
        with open('lvl.json', 'w') as lvl:
            json.dump(data, lvl)
    elif c == 'g':
        with open('lvl.json', 'r') as lvl:
            data = json.load(lvl)
        tick = data['tick'] or 1
        helico.import_data(data['helicopter'])
        field.import_data(data['field'])
        clouds.import_data(data['clouds'])


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()


tick = 1

while True:
    os.system('cls')
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print('TICK', tick,)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update_clouds()


