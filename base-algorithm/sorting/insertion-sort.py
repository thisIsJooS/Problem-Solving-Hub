arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):       # 인덱스 i부터 1까지 감소하며 반복
        if arr[j-1] > arr[j]:           # 앞에야 나보다 크면 자리 바꾸자
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:                       # 앞에야 나보다 작네 거기 있어라
            break

print(arr)
