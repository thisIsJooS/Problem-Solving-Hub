# https://school.programmers.co.kr/learn/courses/30/lessons/62050

from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def solution(land, height):
    answer = 0

    groups, group_num = get_groups(land, height)

    edges = []

    for comb in combinations(range(group_num), 2):
        num1, num2 = comb
        cost = get_cost_from_to(groups, num1, num2, land)
        if cost != 1e9:
            edges.append((cost, num1, num2))

    edges.sort()
    parent = [i for i in range(group_num)]

    for e in edges:
        c, a, b = e

        if find_parent(parent, a) != find_parent(parent, b):
            answer += c
            union(parent, a, b)

    return answer


def get_cost_from_to(groups, num1, num2, land):
    n = len(groups)

    min_gap = 1e9
    num1_groups = []
    visited = [[False] * n for _ in range(n)]

    # for r in range(n):
    #     for c in range(n):
    #         if groups[r][c] == num1:
    #             num1_groups.append((r, c))

    q = deque()

    for r in range(n):
        for c in range(n):
            if groups[r][c] == num1:
                q.append((r, c))
                break

        if q: break

    start = q[0]
    num1_groups.append((start[0], start[1]))
    visited[start[0]][start[1]] = True

    while q:
        now = q.popleft()
        x, y = now

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            if groups[nx][ny] == num1:
                num1_groups.append((nx, ny))
                visited[nx][ny] = True
                q.append((nx, ny))

    for loc in num1_groups:
        x, y = loc

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if groups[nx][ny] != num2:
                continue

            gap = abs(land[nx][ny] - land[x][y])
            min_gap = min(min_gap, gap)

    return min_gap


def get_groups(land, height):
    n = len(land)
    groups = [[-1] * n for _ in range(n)]

    group_num = 0

    for r in range(n):
        for c in range(n):
            if groups[r][c] == -1:
                q = deque()
                q.append((r, c))
                groups[r][c] = group_num

                while q:
                    now = q.popleft()
                    x, y = now

                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]

                        if not is_valid(n, nx, ny, groups):
                            continue

                        if abs(land[nx][ny] - land[x][y]) <= height:
                            groups[nx][ny] = group_num
                            q.append((nx, ny))

                group_num += 1

    return groups, group_num


def is_valid(n, x, y, groups):
    if not (0 <= x < n and 0 <= y < n):
        return False

    if groups[x][y] != -1:
        return False

    return True


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b