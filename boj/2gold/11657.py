"""
입력받은 값은 edges에 저장
distance 배열 정의

함수 내부에, distance[start] = 0
n번 라운드를 반복하고, 모든 간선에 대해서, distance 배열 고쳐
근데 n-1 번째 라운드에서도 갱신이 되었다면, 음수 순환이 존재한다.

"""

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

INF = int(1e9)
distance = [INF] * (n+1)

def f(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            a, b, c = edges[j]

            if distance[a] != INF and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c

                if i == n-1:
                    return True

    return False

if f(1):
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])