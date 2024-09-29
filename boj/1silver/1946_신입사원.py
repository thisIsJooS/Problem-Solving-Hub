t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))  # (서류심사 성적, 면접 성적)

    arr.sort()
    arr = [a[1] for a in arr]

    target = arr[0]

    answer = 1
    for i in range(1, n):
        if target > arr[i]:
            answer += 1
            target = arr[i]

    print(answer)










