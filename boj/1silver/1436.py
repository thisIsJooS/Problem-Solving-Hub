n = int(input())

arr = [0]
for i in range(666, int(1e8)):
    if '666' in str(i):
        arr.append(i)

    if len(arr) == n+1:
        break


print(arr[n])
