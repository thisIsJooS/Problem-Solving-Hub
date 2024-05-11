from collections import deque, defaultdict

def solution():
    n, m = map(int, input().split())

    roads = [i for i in range(101)]
    for _ in range(n+m):
        a, b = map(int, input().split())
        roads[a] = b

    start = 1
    arr = [1e9 for _ in range(101)]
    arr[start] = 0

    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        for i in range(1, 7):
            next = now+i
            if next > 100:
                continue

            if arr[next] > arr[now] + 1:
                arr[next] = arr[now] + 1
                q.append(roads[next])

            if arr[roads[next]] > arr[now] + 1:
                arr[roads[next]] = arr[now] + 1
                q.append(roads[next])


    # for i in range(101):
    #     print(i, arr[i])
    print(arr[100])

solution()