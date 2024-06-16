# https://school.programmers.co.kr/learn/courses/30/lessons/142085#

def solution(n, k, enemy):
    answer = len(enemy) - 1

    left, right = 0, len(enemy) - 1
    while left <= right:
        mid = (left + right) // 2

        if mid <= k - 1:
            left = mid + 1
            answer = mid
            continue

        game = sorted(enemy[:mid+1], reverse=True)
        total = sum(game[k:])

        if total > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

    return answer + 1