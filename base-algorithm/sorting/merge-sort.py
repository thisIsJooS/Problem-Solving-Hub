def merge(left, right):
    res = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                res.append(left[0])
                left = left[1:]

            else:
                res.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            res.append(left[0])
            left = left[1:]

        elif len(right) > 0:
            res.append(right[0])
            right = right[1:]

    return res


def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr = merge_sort(arr)
print(arr)




""" 살짝 더 간결
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
"""