limit = 1000000

start = 100
target = int(input())
n = int(input())
if n > 0:
    broken = list(map(int, input().split()))
else:
    ret = min(len(str(target)), abs(target - start))
    print(ret)
    exit(0)


ans = abs(target-start)
for i in range(limit):
    is_valid = True

    for c in list(map(int, list(str(i)))):
        if c in broken:
            is_valid = False
            break

    if is_valid:
        ans = min(len(str(i)) + abs(i-target), ans)



print(ans)