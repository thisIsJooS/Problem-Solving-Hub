from collections import deque

string, s = list(input()), list(input())
length = len(string)

arr = deque()

def is_including(arr, s):
    if len(arr) < len(s):
        return False

    for i in range(len(s)):
        if arr[i] != s[i]:
            return False

    return True


for i in range(length-1, -1, -1):
    arr.appendleft(string.pop())

    if is_including(arr, s):
        for _ in range(len(s)):
            arr.popleft()


print(''.join(arr) if arr else "FRULA")
