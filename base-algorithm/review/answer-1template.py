"""
3. quick sort
4. merge sort
5. binary search - recursive
6. binary search - iteration
7. Dijkstra shortest-path algorithm
8. Floyd-Warshall shortest-path algorithm
9. Bellman-Ford
10. Prim - MST
11. Kruskal - MST
12. Topology - sort

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]   # for search
"""

import copy
import heapq
from collections import deque

INF = 1e9

# Sort
def quick_sort(arr):

    def f(arr, start, end):
        if start >= end:
            return

        pivot, left, right = start, start+1, end

        while left <= right:
            while left <= end and arr[pivot] >= arr[left]:
                left += 1
            while right > start and arr[pivot] <= arr[right]:
                right -= 1

            if left > right:
                arr[pivot], arr[right] = arr[right], arr[pivot]
            else:
                arr[left], arr[right] = arr[right], arr[left]

        f(arr, start, right-1)
        f(arr, right+1, end)

    f(arr, 0, len(arr)-1)
    return arr


def merge(left, right):
    res = []

    while left or right:
        if left and right:
            if left[0] < right[0]:
                res.append(left[0])
                left = left[1:]
            else:
                res.append(right[0])
                right = right[1:]
        elif left:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]

    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


arr_for_sort = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('    quick_sort >> ', quick_sort(copy.copy(arr_for_sort)))
print('    merge_sort >> ', merge_sort(copy.copy(arr_for_sort)))
print('=================================================')


# Binary Search
def binary_search_recursive(arr, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid-1)
    else:
        return binary_search_recursive(arr, target, mid+1, end)


def binary_search_iteration(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


arr_for_search = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print('(:4)  binary search (recursive) >> ', binary_search_recursive(copy.copy(arr_for_search), 9, 0, len(arr_for_search)-1))
print('(:4)  binary search (iteration) >> ', binary_search_iteration(copy.copy(arr_for_search), 9, 0, len(arr_for_search)-1))
print('=================================================')


# Shortest Path Algorithm
def _dijkstra():     # start 점은 1로 가정
    data = ['4 7 ', '1 2 4', '1 4 6 ', '2 1 3', '2 3 7', '3 1 5', '3 4 4', '4 3 2']     # (v, e), (a, b, cost)

    start = 1
    v, e = map(int, data[0].split())
    graph = [[] for _ in range(v+1)]
    for d in data[1:]:
        a, b, c = map(int, d.split())
        graph[a].append((b, c))

    distance = [INF] * (v+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (c, b))

    return distance[1:]


def _floyd_warshall():
    data = ['4 7 ', '1 2 4', '1 4 6 ', '2 1 3', '2 3 7', '3 1 5', '3 4 4', '4 3 2']     # (v, e), (a, b, cost)
    v, e = map(int, data[0].split())
    graph = [[INF] * (v+1) for _ in range(v+1)]

    for i in range(v+1):
        graph[i][i] = 0

    for d in data[1:]:
        a, b, cost = map(int, d.split())
        graph[a][b] = cost

    for k in range(1, v+1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph[1:]


def _bellman_ford():
    data = ['3 4', '1 2 4', '1 3 3', '2 3 -1', '3 1 -2']  # (v, e), (a, b, cost)

    v, e = map(int, data[0].split())
    edges = []
    distance = [INF] * (v+1)

    for d in data[1:]:
        a, b, c = map(int, d.split())
        edges.append((a, b, c))

    def bf(start):
        distance[start] = 0

        for i in range(v):      # 전체 v 번의 라운드 반복
            for e in edges:      # 매번 "모든 간선" 확인
                now, b, c = e
                cost = distance[now] + c

                if distance[now] != INF and cost < distance[b]:
                    distance[b] = cost

                    if i == v-1:        # v 번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                        return True

        return False

    cycle = bf(1)
    res = ''
    if not cycle:
        for i in range(2, v+1):
            if distance[i] == INF:
                res += '-1'
            else:
                res += str(distance[i])

    return res


print('(:0486)   Dijkstra Shortest Path Algorithm >> ', _dijkstra())
print('    Floyd-Warshall Shortest Path Algorithm >> ', _floyd_warshall())
print('(:43) Bellman_Ford Shortest Path Algorithm >> ', _bellman_ford())
print('=================================================')
""" Floyd-Warshall Answer
>>  0 4 8 6 
    3 0 7 9 
    5 9 0 4 
    7 11 2 0 
"""


# MST
def prim():
    data = ['7 9', '1 2 29', '1 5 75', '2 3 35', '2 6 34', '3 4 7', '4 6 23', '4 7 13', '5 6 53', '6 7 25']     # (v, e), (a, b, cost)
    v, e = map(int, data[0].split())
    start = 1
    graph = [[] for _ in range(v+1)]

    for d in data[1:]:
        a, b, c = map(int, d.split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = []
    heapq.heappush(q, (0, start))
    visited = set()
    res = 0

    while q:
        dist, now = heapq.heappop(q)

        if now in visited:
            continue

        visited.add(now)
        res += dist

        for v, c in graph[now]:
            heapq.heappush(q, (c, v))

    return res


def kruskal():
    def find_parent(x):
        if parent[x] !=  x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(a, b):
        a = find_parent(a)
        b = find_parent(b)

        if a < b: parent[b] = a
        else:
             parent[a] = b

    data = ['7 9', '1 2 29', '1 5 75', '2 3 35', '2 6 34', '3 4 7', '4 6 23', '4 7 13', '5 6 53', '6 7 25']     # (v, e), (a, b, cost)

    v, e = map(int, data[0].split())
    edges = []
    for d in data[1:]:
        a, b, c = map(int, d.split())
        edges.append((c, a, b))

    parent = [i for i in range(v + 1)]
    edges.sort()
    res = 0

    for e in edges:
        c, a, b = e
        if find_parent(a) != find_parent(b):
            union(a, b)
            res += c

    return res


print('(:159)     Prim MST Algorithm >>', prim())
print('(:159)  Kruskal MST Algorithm >>', kruskal())
print('=================================================')


# Topology Sort
def topology_sort():
    data = ['7 8', '1 2', '1 5', '2 3', '2 6', '3 4', '4 7', '5 6', '6 4']      # 1. (v, e) / 2~. (a, b) : a -> b / 진입차수는 모두 1로 가정

    v, e = map(int, data[0].split())
    graph = [[] for _ in range(v+1)]
    indeg = [0] * (v+1)

    for d in data[1:]:
        a, b = map(int, d.split())
        graph[a].append(b)
        indeg[b] += 1

    q = deque()
    for i in range(1, v+1):
        if indeg[i] == 0:
            q.append(i)

    res = []
    while q:
        now = q.popleft()
        res.append(now)

        for v in graph[now]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return res

    return


print('(:1253647)      Topology Sort >> ', topology_sort())
print('=================================================')
