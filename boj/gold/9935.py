from collections import deque

string = list(input())
length = len(string)
s = list(input())
lens = len(s)


def is_same(arr, s):
    for i in range(lens):
        try:
            if arr[i] != s[i]:
                return False
        except:
            return False

    return True


arr = deque()
for i in range(length-1, -1, -1):
    arr.appendleft(string.pop())

    if is_same(arr, s):
        for _ in range(lens):
            arr.popleft()


print(''.join(arr) if arr else "FRULA")
