"""
인자로 받은 문자열 s 를 계수 정렬로 정렬하여 반환하는 solution() 함수를 구현하라
"""

def solution(s):
    counts = [0] * 26

    for c in s:
        counts[ord(c) - ord('a')] += 1

    string = ''
    for i in range(26):
        string += chr(i+ord('a')) * counts[i]

    return string

print(solution("hello"))        # ehllo
print(solution("algorithm"))    # aghilmort

