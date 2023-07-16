class Node:
    def __init__(self):
        self.data = None
        self.next = None


class Hastable:
    def __init__(self, size):
        self.elems = []
        self.size = size
        self.Q = 0
        for i in range(size):
            self.elems.append(Node())

    def hash(self,key):
        return key% self.size + self.Q
    
    # 1 способ борьбы с коллизией
    def add_1(self,value):
        hash = self.hash(value)
        if self.elems[hash].data is None:
            self.elems[hash].data = value
        else:
            current_node = self.elems[hash]
            while current_node.next is not None:
                current_node = current_node.next
            temp = Node()
            temp.data = value
            current_node.next = temp
############################
    # 2 способ борьбы с коллизией (увеличиваем размер таблицы)

    def add_2(self,value):
        hash = self.hash(value)
        while self.elems[hash].data is not None:
            self.size += 1
            self.Q += 1
            hash = self.hash(value)
        self.elems[hash].data = value


#############################     
    def delete(self, value):
        hash = self.hash(value)
        if self.elems[hash].data is None:
            raise Exception("Такого элемента нет")
        else:
            prev = None
            current_node = self.elems[hash]
            if current_node.data == value:
                self.elems[hash] = Node()
                return
            while current_node.next is not None:
                prev = current_node
                current_node = current_node.next
                if current_node.data ==value:
                    prev.next = None
            raise Exception("Такого элемента нет") 
        
    def find(self,value):
        pass

ht = Hastable(10)
ht.add_2(3)
ht.add_2(14)
ht.add_2(23)

ht.delete(23)
ht.delete(14)
a = 1
