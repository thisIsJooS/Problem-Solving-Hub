n = int(input())

arr = list(map(int, input().split()))

arr.sort()
first = arr[0]
last = arr[-1]

print(last*2 - first*2)