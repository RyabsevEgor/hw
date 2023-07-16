# алгоритмы 9 дерево
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

class BinarySearchThree:
    def __init__ (self):
        self.root = Node()

    def add(self, value):
        if self.root.value is None:
            self.root.value = value
            return
        self.add_data(self.root, value)
    
    def add_data(self, cn, value):
        if cn.value > value:
            if cn.left is None:
                cn.left = Node()
                cn.left.value = value
                cn.left.parent = cn
            else:
                self.add_data(cn.left, value)
        else:
            if cn.right is None:
                cn.right = Node()
                cn.right.value = value
                cn.right.parent = cn
            else:
                self.add_data(cn.right, value)

    def find(self, value):
        if self.root.value is None:
            return False
        if self.root.value == value:
            return True
        
        node = self.find_node(self.root, value)
        if node is None:
            return False
        return True
    def find_node(self, cn, value):
        if cn is None:
            return None
        if cn.value == value:
            return cn
        if cn.value > value:
            res = self.find_node(cn.left, value)
            return res
        else:
            res = self.find_node(cn.right, value)
            return res
    def find_min(self):
        node = self.find_min_node(self.root)
        return node.value

    def find_min_node(self, cn):
        if cn.left is None:
            return cn
        node = self.find_min_node(cn.left)
        return node

    def find_max(self):
        node = self.find_max_node(self.root)
        return node.value

    def find_max_node(self, cn):
        if cn.right is None:
            return cn
        node = self.find_max_node(cn.right)
        return node
    def delete(self, value):
        if (self.root.left is None 
            and self.root.right is None
            and self.root.value == value):
            self.root.value = None
        
        if (self.root.left is not None 
            and self.root.right is None
            and self.root.value == value):
            self.root = self.root.left
            self.root.parent = None

        node = self.find_node(self.root, value)
        if node is None:
            raise Exception('не могу найти узел для удаления')
        self.delete_data(node)

    def delete_data(self, node):
        # если нет детей
        if (node.left is None and node.right is None):
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            return
        # если есть дети

        # если 1 ребенок
        if (node.left is not None and node.right is None):
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            return            
        # если 1 ребенок
        if (node.right is not None and node.left is None):
            if node.parent.right == node:
                node.parent.right = node.right
            else:
                node.parent.left = node.right
            return            
        # если 2 детей
        if (node.left is not None and node.right is not None):
            min_node_of_right = node.left
            if node.parent == node:
                if node.parent.left == node:
                    node.parent.left = min_node_of_right
                else:
                    node.parent.right = min_node_of_right
            else:
                node.value = min_node_of_right.value
                self.delete_data(min_node_of_right)





bst = BinarySearchThree()
bst.add(10)
bst.add(8)
bst.add(9)
bst.add(7)
bst.add(20)
bst.add(19)
bst.add(47)
bst.add(22)
print(bst.find(9), bst.find(19), bst.find(21))
bst.delete(47)
bst.delete(10)
print(bst.find_min(), bst.find_max())
print(bst.find(9),bst.find(19), bst.find(10))

a = 1