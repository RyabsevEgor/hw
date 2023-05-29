class turtle:
  s = 1
  y = 0
  x = 0
  def __init__(self, x,y,s = 1): # начальная позиция и начальный шаг
    self.x = x
    self.y = y
    self.s= s
  def go_up(self):
    self.y += self.s

  def down(self):
    self.y -= self.s  

  def go_left(self):
    self.x -= self.s

  def go_right(self):
    self.x += self.s

  def evolve(self):
    self.s += 1
  
  def degrade(self):
    if self.s == 1:
      return 'Ошибка, s уже минимальный'
    self.s -= 1

  def count_moves(self, x2, y2):
    return x2/self.s + y2/self.s

T = turtle(0, 0)

T.evolve()
T.go_up()
T.go_left()
T.go_left()
T.go_right()
T.degrade()
T.down()

print(T.count_moves(7, 4))