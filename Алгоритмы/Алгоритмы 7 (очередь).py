# очередь 
from time import sleep
class Queue1:
    def __init__(self):
        self.elems = list()
    
    def add(self, value):
        self.elems.append(value)

    def get(self):
        val = self.elems.pop(0)
        return val

    def size(self):
        size = len(self.elems)
        return size
    
#очередь (добавление с конца)
from time import sleep
class Queue2:
    def __init__(self):
        self.elems = list()
    
    def add(self, value):
        self.elems.insert(0, value)

    def get(self):
        val = self.elems.pop()
        return val

    def size(self):
        size = len(self.elems)
        return size
    



queue = Queue2()

for i in range(9, -1, -1):
    queue.add(i)
    print(i, end = ' ')
print()
for i in range(queue.size()):
    val = queue.get()
    print(val)
    sleep(val)

