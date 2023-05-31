from random import randint as rand
def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def randcell(w,h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)


#0 - верх 1 - право 2 - вниз 3 - лево
def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)

