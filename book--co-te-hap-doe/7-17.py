# https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque


def solution(cards1, cards2, goal):
    answer = 'Yes'

    goal = deque(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    while goal:
        front = goal.popleft()

        if cards1 and front == cards1[0]:
            cards1.popleft()
            continue
        elif cards2 and front == cards2[0]:
            cards2.popleft()
            continue
        else:
            return 'No'

    return answer