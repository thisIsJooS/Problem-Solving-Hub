"""
1. selection sort
2. insertion sort
3. quick sort
4. merge sort
5. binary search - recursive
6. binary search - iteration
7. Dijkstra shortest-path algorithm
8. Floyd-Warshall shortest-path algorithm
9. Prim - MST
10. Kruskal - MST
11. Topology - sort

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]            # for sort
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]   # for search
"""

import copy
import heapq
from collections import deque


# Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] >= arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

    return arr


def quick_sort(arr):
    def f(start, end):
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
                arr[right], arr[left] = arr[left], arr[right]

        f(start, right-1)
        f(right+1, start)

    f(0, len(arr)-1)

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

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge(left, right)


arr_for_sort = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print('selection_sort >> ', selection_sort(copy.copy(arr_for_sort)))
print('insertion_sort >> ', insertion_sort(copy.copy(arr_for_sort)))
print('    quick_sort >> ', quick_sort(copy.copy(arr_for_sort)))
print('    merge_sort >> ', merge_sort(copy.copy(arr_for_sort)))
print('=================================================')


# Binary Search
def binary_search_recursive(arr, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, end)
    else:
        return binary_search_recursive(arr, target, start, mid-1)


    return


def binary_search_iteration(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else :
            start  = mid + 1


    return


arr_for_search = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print('(:4)  binary search (recursive) >> ', binary_search_recursive(copy.copy(arr_for_search), 9, 0, len(arr_for_search)-1))
print('(:4)  binary search (iteration) >> ', binary_search_iteration(copy.copy(arr_for_search), 9, 0, len(arr_for_search)-1))
print('=================================================')


# Shortest Path Algorithm
def _dijkstra():     # start 점은 1로 가정
    data = ['4 7 ', '1 2 4', '1 4 6 ', '2 1 3', '2 3 7', '3 1 5', '3 4 4', '4 3 2']     # (v, e), (a, b, cost)
    start = 1
    v, e = map(int, data[0].split())
    mat = [[] for _ in range(v+1)]

    for d in data[1:]:
        a, b, cost = map(int, d.split())
        mat[a].append((b, cost))

    distance = [1e9] * (v+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for v, c in mat[now]:
            cost = dist + c
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


    return distance[1:]


def _floyd_warshall():
    data = ['4 7 ', '1 2 4', '1 4 6 ', '2 1 3', '2 3 7', '3 1 5', '3 4 4', '4 3 2']     # (v, e), (a, b, cost)
    v, e = map(int, data[0].split())
    mat = [[100]*(v+1) for _ in range(v + 1)]
    for d in data[1:]:
        a, b, cost = map(int, d.split())
        mat[a][b] = cost

    for i in range(v+1):
        mat[i][i] = 0


    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])


    return mat[1:]


print('(:0486)   Dijkstra Shortest Path Algorithm >> ', _dijkstra())
print('    Floyd-Warshall Shortest Path Algorithm >> ', _floyd_warshall())
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

    start = 1
    v, e = map(int, data[0].split())
    mat = [[] for _ in range(v+1)]

    for d in data[1:]:
        a, b, cost = map(int, d.split())
        mat[a].append((b, cost))
        mat[b].append((a, cost))

    visited = set()
    q = []
    heapq.heappush(q, (0, start))
    res = 0

    while q:
        dist, now = heapq.heappop(q)

        if now in visited:
            continue

        visited.add(now)
        res += dist

        for v, c in mat[now]:
            if v not in visited:
                heapq.heappush(q, (c, v))


    return res


def kruskal():

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(a, b):
        a = find_parent(a)
        b= find_parent(b)

        if a<b:
            parent[b] = a
        else:
            parent[a] = b
    data = ['7 9', '1 2 29', '1 5 75', '2 3 35', '2 6 34', '3 4 7', '4 6 23', '4 7 13', '5 6 53', '6 7 25']     # (v, e), (a, b, cost)

    start = 1
    v, e = map(int, data[0].split())
    mat = [[] for _ in range(v + 1)]
    parent = [i for i in range(v+1)]
    edges = []
    for d in data[1:]:
        a, b, cost = map(int, d.split())
        edges.append((cost, a, b))
    edges.sort()
    res = 0
    for e in edges:
        c, a, b = e
        if find_parent(a) != find_parent(b):
            union(a ,b)
            res += c

    return res


print('(:159)     Prim MST Algorithm >>', prim())
print('(:159)  Kruskal MST Algorithm >>', kruskal())
print('=================================================')


# Topology Sort
def topology_sort():
    data = ['7 8', '1 2', '1 5', '2 3', '2 6', '3 4', '4 7', '5 6', '6 4']      # 1. (v, e) / 2~. (a, b) : a -> b / 진입차수는 모두 1로 가정

    v, e = map(int, data[0].split())
    mat = [[] for _ in range(v + 1)]
    indeg = [0] * (v+1)

    for d in data[1:]:
        a, b= map(int, d.split())
        mat[a].append(b)
        indeg[b] += 1

    q = deque()
    for i in range(1, v+1):
        if indeg[i] == 0:
            q.append(i)

    res = []
    while q:
        now = q.popleft()

        res.append(now)

        for v in mat[now]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)


    return res


print('(:1253647)      Topology Sort >> ', topology_sort())
print('=================================================')
