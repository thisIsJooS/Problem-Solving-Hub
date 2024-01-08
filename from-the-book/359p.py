arr = []
for _ in range(int(input())):
    a, b, c, d = list(input().split())
    arr.append((a, int(b), int(c), int(d)))

# 이름, 국 , 영 , 수

arr.sort()
arr.sort(key = lambda x: x[3], reverse=True)
arr.sort(key = lambda x:x[2])
arr.sort(key = lambda x:x[1], reverse=True)

for a in arr:
    print(a[0])