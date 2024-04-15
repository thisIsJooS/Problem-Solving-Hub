# https://school.programmers.co.kr/learn/courses/30/lessons/92343#

from collections import deque


def solution(info, edges):
    tree = [[] for _ in range(len(info))]

    for edge in edges:
        tree[edge[0]].append(edge[1])

    max_sheep = 0

    # 현재 위치, 양의 수, 늑대 수, 이전까지 인접하고 있는 노드들
    q = deque([(0, 1, 0, set())])

    while q:
        cur, sheep_cnt, wolf_cnt, adjacent = q.popleft()

        max_sheep = max(max_sheep, sheep_cnt)
        adjacent.update(tree[cur])

        for next_node in adjacent:
            if info[next_node]:  # 늑대
                if sheep_cnt != wolf_cnt + 1:
                    q.append((next_node, sheep_cnt, wolf_cnt + 1, adjacent - {next_node}))

            else:  # 양
                q.append((next_node, sheep_cnt + 1, wolf_cnt, adjacent - {next_node}))

    return max_sheep


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))