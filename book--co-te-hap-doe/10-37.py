# https://school.programmers.co.kr/learn/courses/30/lessons/42861

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


def solution(n, costs):
    answer = 0
    edges = []

    for cost in costs:
        a, b, c = cost
        edges.append((c, a, b))

    edges.sort()
    parent = [i for i in range(n)]

    for e in edges:
        c, a, b = e

        if find_parent(parent, a) != find_parent(parent, b):
            answer += c
            union(parent, a, b)

    return answer