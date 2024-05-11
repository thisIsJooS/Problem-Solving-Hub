def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        return sum(arr) - max(arr)

    val = [1e9] * 4

    for c in [[1, 2], [1, 3], [2, 4], [3, 4]]:
        t1 = [0] + c
        t2 = [5] + c

        val[3] = min(val[3], sum([arr[i] for i in t1]))
        val[3] = min(val[3], sum([arr[i] for i in t2]))

    for c in [[1], [2], [3], [4]]:
        t1 = [0] + c
        t2 = [5] + c

        val[2] = min(val[2], sum([arr[i] for i in t1]))
        val[2] = min(val[2], sum([arr[i] for i in t2]))

    for c in [[1], [4]]:
        t1 = [2] + c
        t2 = [3] + c

        val[2] = min(val[2], sum([arr[i] for i in t1]))
        val[2] = min(val[2], sum([arr[i] for i in t2]))

    val[1] = min(arr)

    answer = 0
    answer += val[1] * ((n-1)*(n-2)*4 + (n-2)**2)
    answer += val[2] * 4 * (2*n-3)
    answer += val[3] * 4

    return answer

print(solution())
