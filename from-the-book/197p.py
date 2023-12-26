n = int(input())
entire = list(map(int, input().split()))
m = int(input())
required = list(map(int, input().split()))

entire.sort()

def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


for r in required:
    index = binary_search(entire, r, 0, n-1)

    print('yes') if index else print('no')


"""
5
8 3 7 9 2
3
5 7 9 
"""