n = int(input())
arr = list(map(int, input().split()))

start, end = 0, n-1
def f(start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        elif mid < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

print(f(start, end))

"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""