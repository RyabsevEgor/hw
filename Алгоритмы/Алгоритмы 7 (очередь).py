# очередь
from time import sleep
class Queue:
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
    
queue = Queue()

for i in range(10):
    queue.add(i)

for i in range(queue.size()):
    val = queue.get()
    print(val)
    sleep(val)