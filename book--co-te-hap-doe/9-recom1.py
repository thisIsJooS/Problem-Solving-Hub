# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0

    start, end = 0, n // len(times) * max(times)

    while start <= end:
        mid = (start + end) // 2

        if sum([mid // i for i in times]) < n:  # 아직 다 처리 못함
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

    return answer