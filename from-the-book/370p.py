from bisect import *

def solution(words, queries):
    N = len(words)

    arr = [[] for _ in range(10001)]
    arr_reverse = [[] for _ in range(10001)]

    for w in words:
        arr[len(w)].append(w)
        arr_reverse[(len(w))].append(w[::-1])

    for i in range(10001):
        arr[i].sort()
        arr_reverse[i].sort()

    answer = []

    for query in queries:
        Q = len(query)

        if query[0] != '?':
            ans = count_range(arr[Q], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            ans = count_range(arr_reverse[Q], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))

        answer.append(ans)


    return answer


def count_range(arr, left, right):
    left = bisect_left(arr, left)
    right = bisect_right(arr, right)

    return right - left