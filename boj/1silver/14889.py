import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

res = 1e9
arr = [i for i in range(n)]
from itertools import combinations
def get_score(team):
    score = 0
    for comb in combinations(team, 2):
        a, b  = comb
        score += mat[a][b] + mat[b][a]

    return score


def f(team, now):
    global res

    if len(team) == n//2:
        other_team = [x for x in arr if x not in team]
        res = min(res, abs(get_score(team) - get_score(other_team)))
        return

    for i in range(now, n):
        team.append(i)
        f(team, i+1)
        team.pop()


f([], 0)
print(res)