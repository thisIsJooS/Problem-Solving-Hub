# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


# 두 원소가 속한 집합을 합치기
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    edges = []
    total  = 0
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        total += c

    edges.sort()
    parent = [i for i in range(n+1)]
    for e in edges:
        c, a, b = e

        if find_parent(parent, a) != find_parent(parent, b):
            total -= c
            union(parent, a, b)


    print(total)
