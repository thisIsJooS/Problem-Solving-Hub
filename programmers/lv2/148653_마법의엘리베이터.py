# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(num):
    answer = 0

    while True:
        if num == 0:
            return answer

        last = num % 10

        if last <= 4:
            answer += last
            num = num // 10

        elif last >= 6:
            answer += 10 - last
            num = num // 10 + 1

        elif last == 5:
            if num < 10:
                answer += last
                num = num // 10
            else:
                vice = (num // 10) % 10
                if vice >= 5:
                    answer += last
                    num = num // 10 + 1
                else:
                    answer += last
                    num = num // 10
