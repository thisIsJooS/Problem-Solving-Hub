# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)

    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] > numbers[i + 1]:
            if answer[i + 1] == -1:
                answer[i] = answer[i + 1]

            elif numbers[i] >= answer[i + 1]:
                for k in range(i + 1, len(numbers)):
                    if answer[k] > numbers[i]:
                        answer[i] = answer[k]
                        break
            else:
                answer[i] = answer[i + 1]


        elif numbers[i] < numbers[i + 1]:
            answer[i] = numbers[i + 1]

        elif numbers[i] == numbers[i + 1]:
            answer[i] = answer[i + 1]

    return answer