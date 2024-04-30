# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque


def solution(people, limit):
    answer = 0

    people.sort(reverse=True)

    now = 0

    q = deque(people)

    while q:
        if not now:  # 아무도 안 타 있으면
            answer += 1
            p = q.popleft()
            now += p
        else:  # 1명이 지금 타있으면
            if now + q[-1] <= limit:  # 나머지 한명이 탈 수 있으면
                q.pop()

            now = 0

    return answer