# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque


def solution(graph):
    answer = 0

    n = len(graph)
    m = len(graph[0])
    visited = [[False] * m for _ in range(n)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    group = {0: 0}
    group_num = 3

    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0 or visited[r][c]:
                continue

            q = deque()
            q.append((r, c))
            visited[r][c] = True
            graph[r][c] = group_num
            cnt = 1

            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if not (0 <= nx < n and 0 <= ny < m): continue
                    if visited[nx][ny]: continue

                    if graph[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        graph[nx][ny] = group_num
                        cnt += 1

            group[group_num] = cnt
            group_num += 1

    for c in range(m):
        tmp = set()
        for r in range(n):
            tmp.add(graph[r][c])

        answer = max(answer, sum([group[num] for num in tmp]))

    return answer