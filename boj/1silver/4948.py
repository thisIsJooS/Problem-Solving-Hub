import math, sys
input = sys.stdin.readline

def is_prime(n):
    if n == 2:
        return True

    if n%2==0 or n<=1:
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True


while True:
    n = int(input())
    if n==0: exit(0)

    cnt = 0
    for i in range(n+1, 2*n+1):
        if is_prime(i):
            cnt += 1

    print(cnt)
