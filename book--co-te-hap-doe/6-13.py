# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = 0
    height = len(board)

    stack = []

    for m in moves:
        for h in range(height):
            if board[h][m-1] == 0:
                continue

            # 제일 위에꺼 닿음
            pick = board[h][m-1]
            board[h][m-1] = 0

            if stack and stack[-1] == pick:
                answer += 2
                stack.pop()
            else:
                stack.append(pick)
            break

    return answer