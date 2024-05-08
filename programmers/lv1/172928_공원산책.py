# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    direction = {'E': 2, 'W': 3, 'S': 0, 'N': 1}

    n = len(park)
    m = len(park[0])

    start = (0, 0)

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                start = (i, j)
                break

    for route in routes:
        d, v = route.split()
        v = int(v)

        nx, ny = start

        for _ in range(v):
            nx, ny = nx + dx[direction[d]], ny + dy[direction[d]]

            if not (0 <= nx < n and 0 <= ny < m):
                break

            if park[nx][ny] == 'X':
                break
        else:
            start = (nx, ny)

    return list(start)