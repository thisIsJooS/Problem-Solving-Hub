import sys
sys.setrecursionlimit(10**6)

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

# [50, 30, 24, 5, 28, 45, 98, 52, 60]

def f(start, end):
    if start > end:
        return

    mid = end + 1

    for i in range(start+1, end+1):
        if arr[start] < arr[i]:
            mid = i
            break

    f(start+1, mid-1)
    f(mid, end)
    print(arr[start])


f(0, len(arr)-1)
