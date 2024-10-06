from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 상어의 초기 위치값 추출
start = None
for i in range(n):
    if 9 in graph[i]:
        start = (i, graph[i].index(9))
        break


# 상어크기, 먹은 횟수, 시간 초기화
shark_size, ate, time = 2, 0, 0


# 물고기 탐색
while True:
    q = deque([(start[0], start[1], 0)])      # x, y, 이동거리
    closest = 1e9                           # 먹이를 먹을 수 있는 가장 가까운 거리
    candidates = []                       # 같은 거리일 경우 이동 가능한 좌표 저장

    visited = [[False]*n for _ in range(n)] # 방문 처리를 위한 배열
    visited[start[0]][start[1]] = True

    while q:
        x, y, dist = q.popleft()

        if dist > closest:          # 이미 구한 가장 가까운 거리보다 크다면, 탐색 중지
            break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not (0<=nx<n and 0<=ny<n):       # 범위를 벗어나면 pass
                continue

            if graph[nx][ny] > shark_size:      # 상어보다 크면 pass
                continue

            if visited[nx][ny]:                 # 이미 방문했으면 pass
                continue

            visited[nx][ny] = True              # 방문 처리

            # 상어 크기보다 작고, 0이 아닐 때
            if graph[nx][ny] < shark_size and graph[nx][ny] in (1, 2, 3, 4, 5, 6):
                # closest 가 구해지지 않았거나, 같을 경우
                if closest == 1e9 or dist+1 == closest:
                    closest = dist + 1
                    candidates.append((nx, ny, closest))

            else:                   # 먹을 친구를 찾았으면 거기서 탐색을 더 할 필요는 없다.
                q.append((nx, ny, dist+1))

    if not candidates:      # 더 이상 먹이가 없으면, 끝낸다.
        print(time)
        break

    candidates.sort()       # 같은 거리일 경우, 위-왼쪽이 우선이므로 좌표를 정렬해준다.
    target = candidates[0]      # 정렬하면 첫번째 원소가 target 이 된다.

    graph[start[0]][start[1]] = 0
    graph[target[0]][target[1]] = 9
    start = target
    ate += 1
    time += target[2]

    if ate == shark_size:       # 자신의 크기만큼 먹으면 크기가 증가한다.
        shark_size += 1
        ate = 0