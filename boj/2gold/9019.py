from collections import deque
import sys
input = sys.stdin.readline

def f():
    INF = 1e9
    distance = [INF] * 10001

    a, b = map(int, input().split())

    q = deque()
    distance[a] = 0
    q.append(('', a))
    visited = set()

    ans = None

    while q:
        path, now = q.popleft()

        next_list = [D(now), S(now), L(now), R(now)]
        command_list = ['D', 'S', 'L', 'R']
        for i in range(4):
            next = next_list[i]

            if next in visited:
                continue

            visited.add(next)
            q.append((path+command_list[i], next))

            if next == b:
                ans = path+command_list[i]
                break

        else:
            continue
        break

    print(ans)



def D(n):
    return (2*n) % 10000

def S(n):
    if n != 0:
        return n - 1
    return 9999

def L(n):
    front = n % 1000
    back = n // 1000
    res = front * 10 + back
    return res

def R(n):
    front = n % 10
    back = n // 10
    res = front * 1000 + back
    return res


for _ in range(int(input())):
    f()