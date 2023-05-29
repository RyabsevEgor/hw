class Cassa:
  cash = 0
  def __init__(self, c):
    self.cash = c

  def top_up(self, X):
    self.cash += X
  
  def count_1000(self):
    return self.cash // 1000

  def take_away(self, X):
    if X > self.cash:
      return 'Недостаточно денег'
    self.cash -= X

C = Cassa(10000)


C.top_up(5500)
C.take_away(100)
print(C.count_1000())
print(C.cash)