# https://school.programmers.co.kr/learn/courses/30/lessons/81303?language=python3
# 정답이지만 시간초과

def solution(n, cur, cmd):
    answer = ['O'] * n

    stack = []

    for c in cmd:
        c = c.split(' ')

        # C 혹은 Z 일 경우
        if len(c) == 1:
            c = c[0]
            if c == 'C':
                answer[cur] = 'X'
                stack.append(cur)

                if is_last(answer, cur):
                    cur = next_up(answer, cur)
                else:
                    cur = next_down(answer, cur)


            elif c == 'Z':
                z = stack.pop()
                answer[z] = 'O'

        elif len(c) == 2:
            dir, r = c[0], int(c[1])

            if dir == 'D':
                for _ in range(r):
                    cur = next_down(answer, cur)
            else:
                for _ in range(r):
                    cur = next_up(answer, cur)

    answer = ''.join(answer)

    return answer


def is_last(arr, cur):
    for i in range(cur + 1, len(arr)):
        if arr[i] == 'O':
            return False

    return True


def next_up(arr, cur):
    cur -= 1
    while arr[cur] == 'X':
        cur -= 1

    return cur


def next_down(arr, cur):
    cur += 1
    while arr[cur] == 'X':
        cur += 1

    return cur