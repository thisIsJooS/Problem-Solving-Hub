n, b = map(int, input().split())

t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = ''

while n > 0 :
    res += str(t[n % b])
    n = n // b

print(res[::-1])