"""
1. 순열
2. 조합 
3. 중복순열
4. 중복조합
5. Linked List
6. Stack
7. Queue
8. 이진 트리의 순회

"""
from collections import deque

# 1. 순열
def permutations(arr, r):
    result = []

    # 기본 케이스 : 순열의 길이가 0일 때 빈 배열 반환
    if r == 0:
        return [[]]

    # 재귀적으로 각 숫자를 고정시키고 나머지 숫자들의 순열을 구함
    for i in range(len(arr)):
        # 현재 요소를 고정시키고 나머지 요소들을 추출
        current = arr[i]
        remaining = [a for a in arr if a != arr[i]]

        # 길이가 r-1 인 나머지 요소들의 순열을 구함
        for perm in permutations(remaining, r-1):
            result.append([current] + perm)

    return result


# 2. 조합
def combinations(arr, r):
    result = []

    # 기본 케이스 : 조합의 길이가 0일 때 빈 배열을 반환
    if r == 0:
        return [[]]

    # 재귀적으로 각 숫자를 고정시키고 나머지 숫자들의 조합을 구함
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[i+1:]       # 중복 방지를 위해 현재 숫자 이후의 숫자만 고려

        # 길이가 r-1 인 나머지 숫자들의 조합을 구함
        for comb in combinations(remaining, r-1):
            result.append([current] + comb)

    return result


# 중복순열
def permutations_with_replacement(arr, r):
    result = []

    # 기본 케이스 : 중복 순열의 길이가 0일 때 빈 배열을 반환
    if r == 0:
        return [[]]

    # 재귀적으로 각 숫자를 고정시키고 나머지 숫자들의 중복 순열을 구함
    for i in range(len(arr)):
        current = arr[i]

        # 길이가 r-1 인 중복 순열을 구함 (같은 숫자를 다시 사용할 수 있음)
        for perm in permutations_with_replacement(arr, r-1):
            result.append([current] + perm)

    return result


# 중복조합
def combinations_with_replacement(arr, r):
    result = []

    # 기본 케이스 : 중복 조합의 길이가 0일 때 빈 배열을 반환
    if r == 0:
        return [[]]

    # 재귀적으로 각 숫자를 고정시키고 나머지 숫자들의 중복 조합을 구함
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[i:]     # 중복 조합에서는 자신 이후의 요소뿐만 아니라 자신도 다시 고려

        # 길이가 r-1 인 중복 조합을 구함
        for comb in combinations_with_replacement(remaining, r-1):
            result.append([current] + comb)

    return result


print(f'==> 1, 2, 3, 4 : 순열, 조합, 중복순열, 중복조합')
print(f'   순열: {permutations([1, 2, 3, 4], 2)}')
print(f'   조합: {combinations([1, 2, 3, 4], 2)}')
print(f' 중복순열: {permutations_with_replacement([1, 2, 3, 4], 2)}')
print(f' 중복조합: {combinations_with_replacement([1, 2, 3, 4], 2)}')
print("\n***********************************************************")


# 5. Linked List
"""
Operation
1. empty() -> Boolean
2. size() -> Integer
3. add_first(data)
4. add_last(data)
5. insert_after(data, node)
6. insert_before(data, node)
7. search_forward(target) -> node
8. search_backward(target) -> node
9. delete_first()
10. delete_last()
11. delete_node(node)
"""

class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    # @property : getter 메서드를 정의한다. 외부에서 data 에 접근할 때 마치 직접 접근하는 것처럼 보이지만, 실제로는 이 메서드가 호출된다.
    @property
    def data(self):
        return self.__data

    # @data.setter : 외부에서 해당 속성에 값을 할당할 때 호출된다. node.data = 10 호출 시 이 메서드가 호출된다.
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를
        # 저장하지 않는 노드이다. 이를 더미 노드라고 한다.
        self.head = Node()
        self.tail = Node()

        # 초기화. head 와 tail 을 연결한다
        self.head.next = self.tail
        self.tail.prev = self.head

        # 데이터 개수를 저장할 변수이다.
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1

    def add_last(self, data):
        new_node = Node(data)

        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size += 1

    # 3 -> 5    /  (node)3 -> 4 -> 5
    def insert_after(self, data, node):
        new_node = Node(data)

        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1

    def insert_before(self, data, node):
        new_node = Node(data)

        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = new_node
        node.prev = new_node

        self.d_size += 1

    def search_forward(self, target):
        cur = self.head.next    # 첫 번째 노드부터 시작하므로 head.next 를 가리킨다.

        while cur is not self.tail:
            if cur.data == target:
                return cur

            cur = cur.next

        return None

    def search_backward(self, target):
        cur = self.tail.prev

        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.prev

        return None

    # 리스트의 첫 번째 데이터 노드를 삭제한다.
    def delete_first(self):
        if self.empty():
            return

        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1


dll = DoubleLinkedList()
print("==> 5. Linked List")
print("데이터 삽입 - add_first")
dll.add_first(2)
dll.add_first(1)

print("데이터 삽입 - add_last")
dll.add_last(3)
dll.add_last(5)

print(f"data size(4) : {dll.size()}")
print(f"all datas (1 2 3 5) : ", end = ' ')
cur = dll.head.next
while cur != dll.tail:
    print(cur.data, end=" ")
    cur = cur.next
print("\n")

print("데이터 삽입 - insert_after")
node_3 = dll.search_forward(3)
dll.insert_after(4, node_3)  # 3 다음에 4 추가

print(f"data size(5) : {dll.size()}")
print(f"all datas (1 2 3 4 5) : ", end = ' ')
cur = dll.head.next
while cur != dll.tail:
    print(cur.data, end=" ")
    cur = cur.next
print("\n")

print("데이터 삽입 - insert_before")
node_4 = dll.search_forward(4)
dll.insert_before(4, node_4)  # 4 앞에 4 추가 (중복 데이터)

print(f"data size (6) : {dll.size()}")
print(f"all datas (1 2 3 4 4 5) : ", end = ' ')
cur = dll.head.next
while cur != dll.tail:
    print(cur.data, end=" ")
    cur = cur.next
print("\n")

print("데이터 3 탐색")
result_node = dll.search_forward(3)
if result_node:
    print(f"데이터 탐색 결과 : {result_node.data}")
else:
    print("데이터 탐색 실패")

print("데이터 5 삭제 - delete_node")
node_5 = dll.search_forward(5)
if node_5:
    dll.delete_node(node_5)

print(f"data size (5) : {dll.size()}")
print(f"all datas (1 2 3 4 4) : ", end = ' ')
cur = dll.head.next
while cur != dll.tail:
    print(cur.data, end=" ")
    cur = cur.next
print('')
print("\n***********************************************************")

# 6. Stack
"""
Operation
1. empty() -> Boolean
2. push(data)
3. pop() -> element
4. peek() -> element
"""
class Stack:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        return self.container.pop()

    def peek(self):
        if self.empty():
            return None

        return self.container[-1]


print("==> 6. Stack")
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("stack push (1, 2, 3, 4, 5)")
print(f"stack peek 결과 (5) : {s.peek()}")
print("stack pop 결과 (5, 4, 3, 2, 1) : ", end = '')
while not s.empty():
    print(s.pop(), end=' ')
print('\n')
print("***********************************************************")


# 7. Queue
"""
Operation
1. is_empty() -> Boolean
2. is_full() -> Boolean
3. enqueue(data)
4. dequeue() -> element
5. peek() -> element
"""

class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[0]


print("==> 7. Queue")
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("enqueue (1, 2, 3, 4, 5)")
print(f"queue peek 결과 (1) : {q.peek()}")
print("dequeue 결과 (1, 2, 3, 4, 5) : ", end = '')
while not q.empty():
    print(q.dequeue(), end=' ')
print('\n')
print("***********************************************************")


# 8. 이진 트리의 순회 - 전위 순회 (preorder)
class TreeNode:
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


def preorder(cur):
    # 현재 노드가 empty node 라면
    if not cur:
        return

    # 방문
    print(cur.data, end=' ')
    preorder(cur.left)
    preorder(cur.right)


n1 = TreeNode(1);n2 = TreeNode(2);n3 = TreeNode(3);n4 = TreeNode(4);n5 = TreeNode(5);n6 = TreeNode(6);n7 = TreeNode(7)
n1.left = n2; n1.right = n3
n2.left = n4; n2.right = n5
n3.left = n6; n3.right = n7

print("==> 8. preorder")
print("preorder 결과 (1 2 4 5 3 6 7) : ", end='')
preorder(n1)
print('\n')

# 9. 이진 트리의 순회 - 레벨 순서 조회 (levelorder)
def levelorder(cur):
    q = deque()

    q.append(cur)
    while q:
        cur = q.popleft()

        print(cur.data, end=' ')

        # 현재 노드의 왼쪽 자식이 있다면 큐에 추가
        if cur.left:
            q.append(cur.left)

        # 현재 노드의 오른쪽 자식이 있다면 큐에 추가
        if cur.right:
            q.append(cur.right)




print("==> 9. levelorder")
print("levelorder 결과 (1 2 3 4 5 6 7) : ", end='')
levelorder(n1)
print()