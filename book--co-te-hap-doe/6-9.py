# 10진수를 2진수로 변환하기

"""
10 -> 1010
27 -> 11011
12345 -> 11000000111001
"""

def f(n):
    arr = ''
    while n > 0:
        arr += str(n % 2)
        n //= 2

    return arr[::-1]

print(f(10))
print(f(27))
print(f(12345))