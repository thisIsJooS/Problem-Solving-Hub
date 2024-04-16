# https://school.programmers.co.kr/learn/courses/30/lessons/42892

from collections import deque

class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info = info        # 노드의 좌표
        self.left = left        # 노드의 왼쪽 자식 노드
        self.right = right      # 노드의 오른쪽 자식 노드
        self.num = num          # 노드의 번호

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


# 이진 트리 생성 함수
def make_BT(nodeinfo):
    nodes = [i for i in range(1, len(nodeinfo) + 1)]
    nodes.sort(key=lambda x : (nodeinfo[x-1][1], -nodeinfo[x-1][0]), reverse = True)

    root = None
    for i in range(len(nodes)):
        if root is None:
            root = Node(nodeinfo[nodes[0] - 1], nodes[0])
        else:
            parent = root
            node = Node(nodeinfo[nodes[i] - 1], nodes[i])

            while True:
                # 부모 노드의 x 좌표가 더 크면 왼쪽으로
                if node.info[0] < parent.info[0]:
                    if parent.has_left():
                        parent = parent.left
                        continue
                    parent.left = node
                    break

                # 부모 노드의 x 좌표가 더 작거나 같으면 오른쪽으로
                else:
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = node
                    break

    return root


# 전위 순회 함수
def pre_order(root, answer):
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        answer[0].append(node.num)
        stack.append(node.right)
        stack.append(node.left)


# 후위 순회 함수
def post_order(root, answer):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()

        if node is None:
            continue
        if visited:
            answer[1].append(node.num)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))


# 주어진 좌표 정보를 이용하여 이진 트리를 생성하고, 전위 순회와 후위 순회한 결과를 반환한다.
def solution(nodeinfo):
    answer = [[], []]
    root = make_BT(nodeinfo)
    pre_order(root, answer)
    post_order(root, answer)

    return answer