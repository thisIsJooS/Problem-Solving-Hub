# N 을 K 개 정수의 합으로 나타내라. 정수의 최대값은 M 이다.
# 예 : 8 = 1 + 4 + 3

def partition(N, K, M):
    res = []

    def g(n, k, m, pre, res):
        if k <= 1:
            if 0 <= n <= m:
                res.append(pre + [n])
            return

        for i in range(min(n, m) + 1):
            g(n-i, k-1, m, pre+[i], res)

    g(N, K, M, [], res)

    return res

print(*partition(8, 3, 4))

