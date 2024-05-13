expression = input()

stack = []
answer = ''

for char in expression:
    if char.isalpha():      # 알파벳일 경우 바로 정답에 넣는다
        answer += char

    elif char == '(':       # 여는 괄호일 경우 스택에 넣는다
        stack.append(char)

    elif char == ')':       # 닫는 괄호일 경우 여는 괄호가 나올 때까지 정답에 넣는다.
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()         # 여는 괄호를 제거한다.

    elif char in ['+', '-']:    # 덧셈 뺄셈일 경우, 덧셈, 뺄셈, 곱셈, 나눗셈을 모두 정답에 넣는다.
        while stack and stack[-1] in ['+', '-', '*', '/']:
            answer += stack.pop()
        stack.append(char)

    elif char in ['*', '/']:    # 곱셈, 나눗셈일 경우, 곱셈과 나눗셈일 때만 넣는다.
        while stack and stack[-1] in ['*', '/']:
            answer += stack.pop()
        stack.append(char)

while stack:
    answer += stack.pop()

print(answer)