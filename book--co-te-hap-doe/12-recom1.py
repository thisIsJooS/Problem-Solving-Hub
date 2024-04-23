# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = -1

    chars = ['A', 'E', 'I', 'O', 'U']

    def dfs(string):
        nonlocal answer
        answer += 1

        if string == word:
            return True

        if len(string) == 5:
            return False

        for c in chars:
            if dfs(string + c):
                return True

    dfs('')

    return answer