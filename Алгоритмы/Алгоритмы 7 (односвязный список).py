# односвязный список
class Node:
    def __init__(self):
        self.value = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, value):
        if self.head.value is None:
            self.head.value = value
            return

        temp = Node()
        temp.value = value
        # 1 option
        ''''
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = temp 
        '''
        # 2 option
        temp.next = self.head
        self.head = temp
    def lenght(self):
        current_node = self.head
        if self.head is None:
            size = 0
        else:
            size = 1
        while current_node.next is not None:
            current_node = current_node.next
            size += 1
        return size
    
    def find(self, value):
        if self.head.value is not None:
            if self.head.value == value:
                return True
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value == value:
                return True
        return False

    def print(self):
        if self.head.value is None:
            print('пустой список')
            return
        print(self.head.value, end = ' ')
        current_node = self.head
        while current_node.next is not None:
            
            current_node = current_node.next
            print(current_node.value, end = ' ')
        print()

#удаление элемента
    def delete(self,data):

        if self.head.value==data:
            temp=self.head.next
            del self.head
            self.head=temp
        else:
            p=self.head
            if p.value == data:
                del p
            else:
                while p.next.value!=data:
                    p=p.next
            temp=p.next.next
            del p.next
            p.next=temp


LL = LinkedList()
LL.add(9)
LL.add(8)
LL.add(6)
LL.add(7)
LL.add(56)
LL.add(4)
LL.add(11)
print(LL.lenght())

print(LL.find(9))
print(LL.find(24))
LL.print()
LL.delete(11)
LL.print()
a = 10
