import sys

sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    answer = [[]]

    root = make_tree(nodeinfo)

    answer = [root.preorder(), root.postorder()]
    return answer


def make_tree(nodeinfo):
    nums = [i + 1 for i in range(len(nodeinfo))]

    nums.sort(key=lambda x: (-nodeinfo[x - 1][1], nodeinfo[x - 1][0]))
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    root = None
    for i in range(len(nodeinfo)):
        [x, y], num = nodeinfo[i], nums[i]
        if root is None:
            root = Node(x, y, num)
        else:
            parent = root

            while True:
                if x < parent.x:
                    if parent.has_left():
                        parent = parent.left
                        continue
                    parent.left = Node(x, y, num)
                    break
                else:
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = Node(x, y, num)
                    break

    return root


class Node:
    def __init__(self, x, y, num, left=None, right=None):
        self.x = x
        self.y = y
        self.num = num
        self.left = left
        self.right = right

    def has_left(self):
        if self.left is not None:
            return True
        return False

    def has_right(self):
        if self.right is not None:
            return True
        return False

    def preorder(self, res=[]):
        res.append(self.num)

        if self.left is not None:
            self.left.preorder(res)

        if self.right is not None:
            self.right.preorder(res)

        return res

    def postorder(self, res=[]):
        if self.left is not None:
            self.left.postorder(res)

        if self.right is not None:
            self.right.postorder(res)

        res.append(self.num)

        return res

