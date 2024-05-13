import sys
input = sys.stdin.readline

def solution():
    n, m, w = map(int, input().split())

    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))

    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))


    def bf(start):
        distance = [0] * (n+1)
        distance[start] = 0

        for i in range(n):
            for e in edges:
                a, b, c = e
                cost = distance[a] + c

                if distance[b] > cost:
                    distance[b] = cost

                    if i == n-1:
                        return True

        return False

    if bf(1):
        return 'YES'

    return 'NO'


def main():
    t = int(input())

    for _ in range(t):
        print(solution())


main()