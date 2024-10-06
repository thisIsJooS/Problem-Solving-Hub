import copy

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
inputs, points = [], set()

for _ in range(n):
    x, y, d, g = map(int, input().split())
    inputs.append((x, y, d, g))


for start in inputs:
    x, y, d, g = start

    cluster = [(x, y), (x+dx[d], y+dy[d])]      # 0세대, 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다.

    for generation in range(1, g+1):                # 1세대부터 반복문
        ox, oy = cluster[-1][0], cluster[-1][1]     # 끝점(기준점)

        for point in (copy.deepcopy(cluster[:-1]))[::-1]:
            tx, ty = point                              
            nx, ny = ox + (oy - ty), oy + (tx - ox)     # 기준점으로부터 시계방향 90도 돌렸을 경우 좌표 

            if not (0<=nx<=100 and 0<=ny<=100):
                continue

            cluster.append((nx, ny))

    points = points | set(cluster)


ans = 0
for x in range(100):
    for y in range(100):
        a = (x, y)      # a, b, c, d 는 네 꼭짓점의 좌표
        b = (x+1, y)
        c = (x+1, y+1)
        d = (x, y+1)

        if len({a, b, c, d} - points) == 0:     # 네 꼭짓점이 드래곤커브에 다 포함 되는가?
            ans += 1


print(ans)



