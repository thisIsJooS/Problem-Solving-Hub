class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)


    # 문자열 삽입
    def insert(self, string):
        cur_node = self.head

        # 삽입할 String 각각의 문자에 대해 자식 Node를 만들며 내려간다
        for char in string:
            # 자식 Node 들 중 같은 문자가 없으면 Node 새로 생성
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)

            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            cur_node = cur_node.children[char]

        # 문자열이 끝난 지점의 노드의 data 값에 해당 문자열을 표시
        cur_node.data = string


    # 문자열이 존재하는지 탐색
    def search(self, string):
        # 가장 아래에 있는 노드에서부터 탐색을 시작한다.
        cur_node = self.head

        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False

        # 탐색이 끝난 후에 해당 노드의 data 값이 존재한다면 문자가 있다는 뜻
        if cur_node.data is not None:
            return True

