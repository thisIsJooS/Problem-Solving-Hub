class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self, res=[]):
        res.append(self.val)

        if self.left is not None:
            self.left.preorder(res)

        if self.right is not None:
            self.right.preorder(res)

        return res


    def inorder(self, res=[]):
        if self.left is not None:
            self.left.inorder(res)

        res.append(self.val)

        if self.right is not None:
            self.right.inorder(res)

        return res

    def postorder(self, res=[]):
        if self.left is not None:
            self.left.postorder(res)

        if self.right is not None:
            self.right.postorder(res)

        res.append(self.val)

        return res


n  = int(input())
root = None

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nodes = {char: Node(char) for char in chars}

for _ in range(n):
    line = input()
    a, b, c = line.split()

    if b != '.':
        nodes[a].left = nodes[b]
    if c != '.':
        nodes[a].right = nodes[c]


def preorder(root):
    stack = [root]
    res = ''

    while stack:
        node = stack.pop()

        if node is None:
            continue

        res += node.val
        stack.append(node.right)
        stack.append(node.left)

    return res


def inorder(root):
    stack = [(root, False)]
    res = ''

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if visited:
            res += node.val
        else:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))

    return res


def postorder(root):
    stack = [(root, False)]
    res = ''

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if visited:
            res += node.val
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return res


print(preorder(nodes['A']))
# print(nodes['A'].preorder())

print(inorder(nodes['A']))
# print(nodes['A'].inorder())

print(postorder(nodes['A']))
# print(nodes['A'].postorder())





