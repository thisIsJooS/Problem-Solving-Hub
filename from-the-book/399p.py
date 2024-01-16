import sys
input = sys.stdin.readline


for _ in range(int(input())):
    error = False
    n = int(input())
    graph = [[i] for i in range(n+1)]
    graph[0] = []

    arr = [0] + list(map(int, input().split()))
    for i in range(1, n+1):
        for j in range(1, i):
            graph[arr[i]].append(arr[j])


    for _ in range(int(input())):
        a, b = map(int, input().split())

        if a in graph[b]:
            a, b = b, a

        try:
            graph[a].remove(b)
        except:
            print('IMPOSSIBLE')
            error = True
            break
        graph[b].append(a)


    if error: continue

    graph.sort(key = lambda g : len(g))


    # 확실한 순위를 찾을 수 없을 떄 : 그래프 길이의 개수들이 1, 2, 3,... 순서대로가 아닐 떄
    # 데이터에 일관성이 없을 때 : 그래프를 오름차순으로 정렬했을떄, 앞에꺼 노드들이  다 나오지 않았을 때
    prev = []
    for i in range(1, n+1):
        prev.append(graph[i][0])

        for p in prev:
            if p not in graph[i]:
                print('IMPOSSIBLE')
                error = True
                break

        if error:
            break

    if error:
        continue

    for i in range(1, n+1):
        if len(graph[i]) != i:
            print('?')
            error = True
            break

    if error:
        continue

    for i in range(1, n+1):
        print(graph[i][0], end = ' ')

    print()




