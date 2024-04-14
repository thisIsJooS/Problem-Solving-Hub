# 1. 노드 클래스 정의
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# 3. 이진 탐색 트리 클래스
class BST:
    # 초기에 아무 노드도 없는 상태
    def __init__(self):
        self.root = None

    # 루트 노드부터 시작해서 이진 탐색 트리 규칙에 맞는 위치에 새 노드 삽입
    def insert(self, key):
        # 로트 노드가 없는 경우 새로운 노드를 루트 노드로 추가
        if not self.root:
            self.root = Node(key)
            return

        curr = self.root
        while True:
            # 삽입하려는 값이 현재 노드의 값보다 작은 경우 왼쪽 자식 노드로 이동
            if key < curr.val:
                if curr.left:
                    curr = curr.left
                else:           # 현재 노드의 왼쪽 자식 노드가 없는 경우 새로운 노드 추가
                    curr.left = Node(key)
                    break
            else:
                # 삽입하려는 값이 현재 노드의 값보다 큰 경우 오른쪽 자식 노드로 이동
                if curr.right:
                    curr = curr.right
                else:           # 현재 노드의 오른쪽 자식 노드가 없는 경우 새로운 노드 추가
                    curr.right = Node(key)
                    break


    def search(self, key):
        curr = self.root    # 루트 노드부터 시작

        # 현재 노드가 존재하고, 찾으려는 값과 현재 노드의 값이 같지 않은 경우 반복
        while curr and curr.val != key:
            # 찾으려는 값이 현재 노드의 값보다 작은 경우 왼쪽 자식 노드로 이동
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return curr


def solution(lst, search_list):
    bst = BST()

    for key in lst:
        bst.insert(key)

    result = []
    for search_val in search_list:
        if bst.search(search_val):
            result.append(True)
        else:
            result.append(False)

    return result