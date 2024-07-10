from heapq import heappush, heappop

for _ in range(int(input())):
    length = int(input())
    arr = []
    for i in range(length // 10 + 1):
        arr += list(map(int, input().split()))

    left_heap = []
    right_heap = []

    mids = []
    for i, a in enumerate(arr):
        if len(left_heap) == len(right_heap):
            heappush(left_heap, -a)
        else:
            heappush(right_heap, a)

        if right_heap and -left_heap[0] > right_heap[0]:
            left = heappop(left_heap)
            right = heappop(right_heap)

            heappush(left_heap, -right)
            heappush(right_heap, -left)

        if i % 2 == 0:
            mids.append(-left_heap[0])

    print(len(mids))
    for i in range(len(mids) // 10 + 1):
        print(*mids[i*10:i*10 + 10])
