"""
(())() -> True
((())() -> False
"""

s1 = "(())()"
s2 = "((())()"

from collections import deque

def f(s):
    stack = deque()

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    return True

print(f(s1))
print(f(s2))



