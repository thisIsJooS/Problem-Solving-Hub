# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    global answer
    answer = 0

    def dfs(i, res, numbers, target):
        global answer

        if i == len(numbers):
            if res == target:
                answer += 1
            return

        dfs(i + 1, res + numbers[i], numbers, target)
        dfs(i + 1, res - numbers[i], numbers, target)

    dfs(0, 0, numbers, target)

    return answer