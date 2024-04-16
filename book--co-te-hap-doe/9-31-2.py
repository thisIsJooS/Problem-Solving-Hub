from collections import deque


def solution(info, edges):
    answer = 0

    parent = make_parent_tree(info, edges)

    q = deque()
    start = 0

    # (현재 노드, 양 개수, 늑대 개수, 인접 노드들)
    q.append((start, 1, 0, set(parent[0])))

    while q:
        now, cur_sheep, cur_wolf, adj = q.popleft()

        answer = max(answer, cur_sheep)

        for node in adj:
            if info[node]:  # 늑대일 경우
                if cur_sheep != cur_wolf + 1:
                    q.append((node, cur_sheep, cur_wolf + 1, adj - {node} | set(parent[node])))

            else:  # 양일 경우
                q.append((node, cur_sheep + 1, cur_wolf, adj - {node} | set(parent[node])))

    return answer


def make_parent_tree(info, edges):
    arr = [[] for _ in range(len(info))]

    for e in edges:
        parent, child = e
        arr[parent].append(child)

    return arr