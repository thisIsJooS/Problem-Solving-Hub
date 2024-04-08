# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3

# O(N^2)
def solution1(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[j] < prices[i]:
                break
        answer.append(cnt)

    return answer


# O(N)
def solution(prices):
    n = len(prices)
    answer = [0] * n

    stack = [0]
    for i in range(1, n):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer