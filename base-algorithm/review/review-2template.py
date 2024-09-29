"""
0. bubble sort
1. selection sort
2. insertion sort
3. quick sort
4. merge sort
4.1. counting sort
4.2. radix sort
5. binary search - recursive
6. binary search - iteration
7. Dijkstra shortest-path algorithm
8. Floyd-Warshall shortest-path algorithm
9. Bellman-Ford
10. Prim - MST
11. Kruskal - MST
12. Topology - sort

"""

import copy
import heapq
from collections import deque, defaultdict


# Sort

def bubble_sort(arr):

    return arr


def selection_sort(arr):

    return arr


def insertion_sort(arr):

    return arr


def quick_sort(arr):

    return arr


def merge():
    pass


def merge_sort(arr):

    return


def counting_sort(arr):

    return


def radix_sort(arr):

    return arr


arr_for_sort = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr_for_counting = [5, 5, 3, 4, 5, 1, 0, 4, 1, 3, 0, 2, 4, 2, 3, 0]
arr_for_radix = [15, 27, 64, 25, 50, 17, 39, 28]
print('   bubble_sort >> ', bubble_sort(copy.copy(arr_for_sort)))
print('selection_sort >> ', selection_sort(copy.copy(arr_for_sort)))
print('insertion_sort >> ', insertion_sort(copy.copy(arr_for_sort)))
print('    quick_sort >> ', quick_sort(copy.copy(arr_for_sort)))
print('    merge_sort >> ', merge_sort(copy.copy(arr_for_sort)))
print(' counting_sort >> ', counting_sort(copy.copy(arr_for_counting)))
print('    radix_sort >> ', radix_sort(copy.copy(arr_for_radix)))
print('=================================================')


# Binary Search
def binary_search_recursive(arr, target, start, end):

    return


def binary_search_iteration(arr, target, start, end):

    return


arr_for_search = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print('(:4)  binary search (recursive) >> ', binary_search_recursive(copy.copy(arr_for_search), 9, 0, len(arr_for_search)-1))
print('(:4)  binary search (iteration) >> ', binary_search_iteration(copy.copy(arr_for_search), 9, 0, len(arr_for_search)-1))
print('=================================================')


# Shortest Path Algorithm
def _dijkstra():     # start 점은 1로 가정
    data = ['4 7 ', '1 2 4', '1 4 6 ', '2 1 3', '2 3 7', '3 1 5', '3 4 4', '4 3 2']     # (v, e), (a, b, cost)

    return


def _floyd_warshall():
    data = ['4 7 ', '1 2 4', '1 4 6 ', '2 1 3', '2 3 7', '3 1 5', '3 4 4', '4 3 2']     # (v, e), (a, b, cost)

    return


def _bellman_ford():
    data = ['3 4', '1 2 4 ', '1 3 3 ', '2 3 -1 ', '3 1 -2 ']  # (v, e), (a, b, cost)

    return


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

    return


def kruskal():
    data = ['7 9', '1 2 29', '1 5 75', '2 3 35', '2 6 34', '3 4 7', '4 6 23', '4 7 13', '5 6 53', '6 7 25']     # (v, e), (a, b, cost)

    return


print('(:159)     Prim MST Algorithm >>', prim())
print('(:159)  Kruskal MST Algorithm >>', kruskal())
print('=================================================')


# Topology Sort
def topology_sort():
    data = ['7 8', '1 2', '1 5', '2 3', '2 6', '3 4', '4 7', '5 6', '6 4']      # 1. (v, e) / 2~. (a, b) : a -> b / 진입차수는 모두 1로 가정
    return


print('(:1253647)      Topology Sort >> ', topology_sort())
print('=================================================')
