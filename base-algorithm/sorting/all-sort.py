"""
1. selection-sort
2. insertion-sort
3. quick-sort
4. merge-sort
"""
import copy


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

    return arr


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left, right = start+1, end

    while left <= right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

    return arr


def merge_sort(arr):
    def merge(left, right):
        res = []

        while left or right:
            if left and right:
                if left[0] < right[0]:
                    res.append(left[0])
                    left = left[1:]
                else:
                    res.append(right[0])
                    right = right[1:]

            elif left:
                res.append(left[0])
                left = left[1:]
            elif right:
                res.append(right[0])
                right = right[1:]

        return res

    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)


data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(selection_sort(copy.copy(data)))
print(insertion_sort(copy.copy(data)))
print(quick_sort(copy.copy(data), 0, len(data)-1))
print(merge_sort(copy.copy(data)))
