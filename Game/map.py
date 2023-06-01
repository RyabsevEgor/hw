from utils import randbool
from utils import randcell
from utils import randcell2
'''
0 - поле
1 - дерево
2 - река
3 - госпиталь
4 - магазин
5 - огонь
🟩🚁🌲🌳🔥🌊🏆☁️🌩️⚡🏥🛒🧯🧡⬛ 🟦

'''
CELL_TYPES = '🟩🌲🟦🏥🛒🔥'

class Map:
      
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
    
    def generetae_river(self, l):
        rc = randcell(self.w, self.h)
        print(rc)
        rx, ry = rc[0] , rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2,ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx][ry] = 2
                rx, ry = rx2, ry2
                l-=1

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1


    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool (r, mxr):
                    self.cells[ri][ci] = 1

        
    def print_map(self):
        print('⬛'*(self.w + 2))
        for row in self.cells:
            print('⬛', end = '')
            for cell in row:
                if (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end = '')
            print('⬛')
        print('⬛'*(self.w + 2))

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
   
   
    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5


    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.add_fire()
        




tmp = Map(20, 10)

tmp.generate_forest(6, 10)
tmp.generetae_river(30)
tmp.generetae_river(10)

tmp.print_map()