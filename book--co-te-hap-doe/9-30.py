# https://school.programmers.co.kr/learn/courses/30/lessons/159993#

from collections import deque

def is_valid(x, y, n, m, maps):
    if not (0 <= x < n and 0 <= y < m):
        return False

    if maps[x][y] == 'X':
        return False

    return True


def solution(maps):
    answer = 0

    _start, _lever, _exit = 0, 0, 0
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                _start = (i, j)
            elif maps[i][j] == 'L':
                _lever = (i, j)
            elif maps[i][j] == 'E':
                _exit = (i, j)

    # 레버 찾기
    q, visited = deque(), set()
    q.append((_start[0], _start[1], 0))
    visited.add((_start[0], _start[1]))
    lever_found = False
    first = 0

    while q and not lever_found:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (nx, ny) in visited:
                continue

            if not is_valid(nx, ny, n, m, maps):
                continue

            if maps[nx][ny] == 'L':
                lever_found = True
                first = cnt + 1
                break

            if maps[nx][ny] != 'X':
                q.append((nx, ny, cnt + 1))
                visited.add((nx, ny))

    if not lever_found:
        return -1

    # 출구 찾기
    q, visited = deque(), set()
    q.append((_lever[0], _lever[1], 0))
    visited.add((_lever[0], _lever[1]))
    exit_found = False
    second = 0

    while q and not exit_found:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (nx, ny) in visited:
                continue

            if not is_valid(nx, ny, n, m, maps):
                continue

            if maps[nx][ny] == 'E':
                exit_found = True
                second = cnt + 1
                break

            if maps[nx][ny] != 'X':
                q.append((nx, ny, cnt + 1))
                visited.add((nx, ny))

    if not exit_found:
        return -1

    return first + second

