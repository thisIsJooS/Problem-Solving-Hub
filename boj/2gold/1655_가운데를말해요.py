from heapq import heappush, heappop
import sys
input = sys.stdin.readline

left_heap = []
right_heap = []

for _ in range(int(input())):
    n = int(input())

    if len(left_heap) == len(right_heap):
        heappush(left_heap, -n)
    else:
        heappush(right_heap, n)

    if right_heap and -left_heap[0] > right_heap[0]:
        left = heappop(left_heap)
        right = heappop(right_heap)

        heappush(left_heap, -right)
        heappush(right_heap, -left)

    print(-left_heap[0])