# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        arr = array[i - 1:j]
        arr.sort()
        answer.append(arr[k - 1])

    return answer