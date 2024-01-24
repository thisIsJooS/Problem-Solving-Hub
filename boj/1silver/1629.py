a, b, c = map(int, input().split())

def f(a, b):
    global c
    if b == 1:
        return a % c

    if b % 2 == 1:  # 홀수
        return (a * f(a, b-1)) % c
    else:   # 짝수
        return ((f(a, b//2) % c) ** 2 ) % c

print(f(a, b) % c)
