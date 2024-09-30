n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    stack = []

    for w in word:
        if not stack or w != stack[-1]:
            stack.append(w)

        elif w == stack[-1]:
            stack.pop()
    else:
        if not stack:
            cnt += 1

print(cnt)

