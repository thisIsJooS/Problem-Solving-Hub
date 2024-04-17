# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from collections import Counter


def solution(nums):
    answer = 0

    counter = Counter(nums)

    return min(len(counter.keys()), len(nums) // 2)