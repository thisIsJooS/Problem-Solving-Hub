# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []

    right = 0
    val = sequence[0]
    shortest = 1e9

    for left in range(len(sequence)):
        while val < k and right < len(sequence) - 1:
            right += 1
            val += sequence[right]

        if val == k:
            if right - left + 1 < shortest:
                shortest = right - left + 1
                answer = [left, right]

        val -= sequence[left]

    return answer