import sys
input = sys.stdin.readline

t = int(input())

from collections import deque

def f():
    commands = list(input().rstrip())
    input()
    arr = input().rstrip()
    arr = arr[1:-1]
    if arr:
        arr = list(map(int, arr.split(',')))
        arr = deque(arr)
    else:
        arr = deque()


    pivot = 0       # 0 은 왼쪽, 1 은 오른쪽
    for c in commands:
        if c == 'D':
            if not arr:
                print('error')
                return None

            if pivot == 0:
                arr.popleft()
            else:
                arr.pop()

        else:
            pivot = 1 - pivot

    if pivot and arr:
        tmp = deque()
        while arr:
            tmp.append(arr.pop())
        arr = tmp

    s = '['
    if len(arr) == 1:
        s += f'{arr[0]}'
        s += ']'
        return s
    elif len(arr) == 0:
        s += ']'
        return s
    else:
        for a in arr:
            s += f'{a}'
            s += ','
        s = s[:-1]
        s += ']'
        return s


for _ in range(t):
    ret = f()
    if ret is not None:
        print(ret)