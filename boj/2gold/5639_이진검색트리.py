import sys
sys.setrecursionlimit(10**6)

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def postorder(self, cur=None):
        if cur is None:
            return

        self.postorder(cur.left)
        self.postorder(cur.right)
        print(cur.data)


    def insert(self, key):
        node = Node(key)

        cur = self.root
        if not cur:
            self.root = node
            return

        while True:
            parent = cur
            if key < cur.data:
                cur = cur.left
                if not cur:
                    parent.left = node
                    break

            else:
                cur = cur.right
                if not cur:
                    parent.right = node
                    break


tree = BST()

for a in arr:
    tree.insert(a)

tree.postorder(tree.root)
