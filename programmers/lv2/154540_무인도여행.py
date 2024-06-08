# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque


def solution(maps):
    for i, map in enumerate(maps):
        maps[i] = list(map)

    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if not maps[row][col].isdigit():
                continue

            val = int(maps[row][col])
            q = deque()
            q.append((row, col))
            maps[row][col] = 'O'

            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if not (0 <= nx < len(maps) and 0 <= ny < len(maps[0])):
                        continue

                    if not maps[nx][ny].isdigit():
                        continue

                    val += int(maps[nx][ny])
                    maps[nx][ny] = 'O'
                    q.append((nx, ny))

            answer.append(val)

    return sorted(answer) if answer else [-1]