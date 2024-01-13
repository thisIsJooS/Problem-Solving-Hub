import math

def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0 or n <= 1:
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True




for _ in range(int(input())):
    n = int(input())
    i = n
    while True:
        if is_prime(i):
            print(i)
            break
        i += 1