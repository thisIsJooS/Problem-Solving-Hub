from heapq import *
import sys
input = sys.stdin.readline

t = int(input())

def f():
    k = int(input())
    min_heap, max_heap = [], []
    popped = [False] * k
    for i in range(k):
        a, b = input().rstrip().split()
        b = int(b)

        # I 는 삽입
        if a == 'I':
            heappush(min_heap, (b, i))
            heappush(max_heap, (-b, i))

        # D 1 는 최댓값 삭제
        # D -1 은 최솟값 삭제
        else:
            if b == -1:     # min heap
                while min_heap and popped[min_heap[0][1]]:
                    heappop(min_heap)

                if not min_heap: continue

                num, index = heappop(min_heap)
                popped[index] = True

            else:           # max heap
                while max_heap and popped[max_heap[0][1]]:
                    heappop(max_heap)

                if not max_heap : continue

                num, index = heappop(max_heap)
                popped[index] = True

    while min_heap and popped[min_heap[0][1]]:
        heappop(min_heap)

    while max_heap and popped[max_heap[0][1]]:
        heappop(max_heap)

    # print(min_heap, max_heap, arr, popped)
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')


for _ in range(t):
    f()