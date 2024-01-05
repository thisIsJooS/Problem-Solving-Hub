import time

def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result *= x
    return result


def power(x, n):
    if n == 0:
        return 1        # 종료 조건

    elif n % 2 == 0 :      # n이 짝수일 경우
        return power(x*x, n//2)

    else:               # n이 홀수일 경우
        return x * power(x*x, (n-1)//2)


t1 = time.time()
for i in range(int(1e5)): slow_power(2.0, 500)
t2 = time.time()
for i in range(int(1e5)): power(2.0, 500)
t3 = time.time()

print("  억지 기법 시간 >> ", t2-t1)
print("축소정복기법 시간 >> ", t3-t2)
