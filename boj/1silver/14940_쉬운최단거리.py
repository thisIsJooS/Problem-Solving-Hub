from collections import deque

n, m = map(int, input().split())

# 입력 배열 받기
arr = [list(map(int, input().split())) for _ in range(n)]

# 방문 처리할 똑같은 크기의 2차원 배열
visited = [[False]*m for _ in range(n)]

# 출력 결과를 같은 크기의 2차원 배열, 도달할 수 없는 위치는 -1이 될것이기에 초기값을 -1로
res = [[-1]*m for _ in range(n)]

# 입력 배열중에 2(출발점)의 좌표를 저장할 변수
start = None

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 입력배열에서 2인 좌표는 방문처리, 좌표를 start 변수에 저장, res (결과 배열)에 0으로 대치
# 입력 배열에서 0인 곳은 갈수 없기에 결과 배열에도 0으로 대치
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start = (i, j)
            visited[i][j] = True
            res[i][j] = 0

        if arr[i][j] == 0:
            res[i][j] = 0


# 큐 정의, 시작점의 x,y좌표 그리고 이동 거리 저장. 이동거리는 초기값을 0으로
q = deque()
q.append((start[0], start[1], 0))

while q:
    x, y, dist = q.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        # 배열에서 벗어나면 continue
        if not (0<=nx<n and 0<=ny<m):
            continue

        # 방문했었으면 continue
        if visited[nx][ny]:
            continue

        # 갈수 있는 곳(=1) 이 아니면 continue
        if arr[nx][ny] != 1:
            continue

        # 방문 처리, 결과 배열에 저장
        visited[nx][ny] = True
        res[nx][ny] = dist+1

        # 다음 큐에 저장
        q.append((nx, ny, dist+1))

# 출력
for r in res:
    print(*r)



