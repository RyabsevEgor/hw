from utils import randbool
from utils import randcell
from utils import randcell2
import os
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
TREE_BONUS = 1000
UPGRADE_COST = 5000
LIFE_COST = 10000
class Map:
      
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(4, 10)
        self.generetae_river(30)
        self.generetae_river(10)
        self.generate_upgrade_shoop()
        self.generate_hospital()

    

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    
    def print_map(self, helico, clouds):
        print('⬛'*(self.w + 2))
        for ri in range(self.h):
            print('⬛', end = '')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci]==1 and self.cells[ri][ci] != 3 and self.cells[ri][ci] != 4):
                    print('⬜', end = '')
                elif (clouds.cells[ri][ci]==2 and self.cells[ri][ci] != 3 and self.cells[ri][ci] != 4):
                    print('⚡', end = '')
                elif helico.x == ri and helico.y == ci:
                    print('🚁', end = '')
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end = '')
            print('⬛')
        print('⬛'*(self.w + 2))


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

    def generate_upgrade_shoop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy)):
            self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy), self.cells[cx][cy] != 4):
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool (r, mxr):
                    self.cells[ri][ci] = 1

   
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
        for i in range(10):
            self.add_fire()

    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.maxtank
        if c == 5 and helico.tank > 0:
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if c  == 4 and helico.score >= UPGRADE_COST:
            helico.score -= UPGRADE_COST
            helico.maxtank +=1
        
        if c  == 3 and helico.score >= LIFE_COST:
            helico.score -= LIFE_COST
            helico.lives +=10
        if d == 2:
            helico.lives -=1
            if helico.lives == 0:
                os.system('cls')
                print('ИГРА ОКОНЧЕНА, ВАШ СЧЕТ', helico.score)
                exit(0)


        