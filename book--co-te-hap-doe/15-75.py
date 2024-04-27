# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if j != 0 and j != len(arr[i]) - 1:
                arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
            elif j == 0:
                arr[i][j] += arr[i - 1][j]
            else:
                arr[i][j] += arr[i - 1][j - 1]

    return max(arr[-1])