"""
이진 트리를 표현한 리스트 nodes 를 인자로 받는다
해당 이진 트리에 대해, 전위 중위 후위 순회 결과를 반환하는 solution() 함수를 구현하라

입력
[1, 2, 3, 4, 5, 6, 7]

return
["1245367", "4251637", "4526731"]

BOJ : https://www.acmicpc.net/problem/1991
"""

def solution(nodes):

    return preorder(nodes, 0), inorder(nodes, 0), postorder(nodes, 0)


def preorder(nodes, idx):
    # idx 가 노트 리스트의 길이보다 크면 return
    if idx >= len(nodes):
        return ''

    # 루트 노드를 출력한 다음, 왼쪽 서브 트리와 오른쪽 서브 트리를 재귀 호출하여 출력 순서대로 이어붙임
    ret = str(nodes[idx])
    ret += preorder(nodes, idx*2 + 1)
    ret += preorder(nodes, idx*2 + 2)

    return ret


def inorder(nodes, idx):
    if idx >= len(nodes):
        return ''

    ret = ''
    ret += inorder(nodes, idx*2 + 1)
    ret += str(nodes[idx])
    ret += inorder(nodes, idx*2 + 2)

    return ret


def postorder(nodes, idx):
    if idx >= len(nodes):
        return ''

    ret = ''
    ret += postorder(nodes, idx*2 + 1)
    ret += postorder(nodes, idx*2 + 2)
    ret += str(nodes[idx])

    return ret

print(solution([1, 2, 3, 4, 5, 6, 7]))