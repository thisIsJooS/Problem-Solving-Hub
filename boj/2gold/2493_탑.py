n = int(input())

arr = [500_001] + list(map(int, input().split()))

res = [0] * len(arr)
stack = []

for i in range(len(arr)-1, 0, -1):
    if arr[i-1] < arr[i]:
        stack.append(i)

    if arr[i-1] > arr[i]:
        res[i] = i-1

        while stack:
            if arr[i-1] > arr[stack[-1]]:
                res[stack.pop()] = i-1
            else:
                break

print(*res[1:])