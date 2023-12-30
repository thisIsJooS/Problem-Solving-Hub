from collections import deque

n = int(input())
k = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())        # 사과의 x, y 위치
    graph[x][y] = 1

l = int(input())    # 뱀의 방향 변환 횟수
rotate = deque()
for _ in range(l):
    x, c = input().split()        # x 초가 지난뒤에 L이면 왼쪽, R이면 오른쪽으로 90도 방향 회전
    rotate.append((x, c))

def is_valid(x, y):
    if 0<x<=n and 0<y<=n:
        return True
    return False

x, y = 1, 1
time = 0
q = deque()
q.append((x, y))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
while q:
    time += 1
    nx, ny = x + dx[d], y + dy[d]

    if not is_valid(nx, ny):
        break

    if (nx, ny) in q:
        break

    if graph[nx][ny] != 1:
        q.popleft()
    else:
        graph[nx][ny] = 0

    q.append((nx, ny))

    if rotate and time == int(rotate[0][0]):
        x, c = rotate.popleft()

        if c == 'D':
            d = (d+1) % 4
        else:
            d = (d-1) % 4

    x, y = nx, ny

print(time)