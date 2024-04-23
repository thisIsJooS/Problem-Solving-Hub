# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key

def compare(a, b):
    # 각 수를 문자열로 바꾼 뒤, 조합하여 비교하여 더 큰 수를 반환한다.
    # 예. a=3, b=30 -> t1='330', t2='303' -> int(t1) > int(t2) -> 1 반환

    t1 = int(str(a) + str(b))
    t2 = int(str(b) + str(a))
    return (t1 > t2) - (t1 < t2)


# numbers : [6, 10, 2]
def solution(numbers):
    sorted_nums = sorted(numbers, key = cmp_to_key(lambda a, b : compare(a, b)), reverse=True)

    answer = ''.join(str(x) for x in sorted_nums)
    return '0' if int(answer) == 0 else answer