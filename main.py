# arr[i] = 2*arr[i-1] - 1

# https://www.acmicpc.net/problem/2903

arr = [2]

n = int(input())

for i in range(1, n+1):
    arr.append(2*arr[i-1]-1)

print(arr[-1]**2)