from collections import deque

n = int(input())
arr = deque(list(map(int, input().split())))
tmp = deque()

order = 1

while order != n+1:
    if arr:
        t = arr[0]

        if t == order:
            arr.popleft()
            order += 1

        else:
            if tmp and tmp[-1] == order:
                t = tmp.pop()
                order += 1
            else:
                arr.popleft()
                tmp.append(t)

    else:
        t = tmp.pop()

        if t == order:
            order += 1

        else:
            print('Sad')
            exit(0)

print('Nice')