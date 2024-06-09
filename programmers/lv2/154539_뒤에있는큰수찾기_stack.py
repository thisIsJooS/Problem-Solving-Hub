# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)

    stack = [numbers[-1]]
    for i in range(len(numbers) - 2, -1, -1):
        if stack and numbers[i] >= stack[-1]:
            while stack:
                stack.pop()

                if not stack:
                    stack.append(numbers[i])
                    break

                elif numbers[i] < stack[-1]:
                    answer[i] = stack[-1]
                    stack.append(numbers[i])
                    break

        elif stack and numbers[i] < stack[-1]:
            answer[i] = stack[-1]
            stack.append(numbers[i])

    return answer