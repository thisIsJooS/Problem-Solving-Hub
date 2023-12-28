"""
2개로 분리, 분리된 마을은 다 연결되어 있어야 함
분리되면, 분리된 사이 간선은 없애. 분리된 집합 안에서도 최소신장트리
길을 모두 없애고 나머지 길의 최소
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
for _ in range(m):
    a, b, c = map(int, input().split()) # A와 B를 사이 거리는 C
    edges.append((c, a, b))
edges.sort()

mst = []
for e in edges:
    c, a, b = e
    if find_parent(a) != find_parent(b):
        mst.append(c)
        union(a, b)

print(sum(mst) - max(mst))


"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
>> 8
"""
