N, R, C = map(int, input().split())
M = 2 ** N

"""
1 2 
3 4
"""

def f(M, start, r, c):
    if M == 1:
        return start

    if r < M//2:    # 1, 2
        if c < M//2:    # 1
            return f(M//2, start, r, c)
        elif c >= M//2:           # 2
            return f(M//2, start + M**2 // 4, r, c - M//2)

    elif r >= M//2:     # 3, 4
        if c < M//2 :   # 3
            return f(M//2, start + M**2 // 4 * 2, r - M//2, c)
        elif c >= M//2:
            return f(M//2, start + M**2 // 4 * 3, r - M//2, c - M//2)


print(f(M, 0, R, C))

