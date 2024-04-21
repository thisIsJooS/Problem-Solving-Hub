def is_valid(hp, data):
    a, b = data

    if hp < a:
        return False

    return True


def dfs(hp, dgs, visited):
    global answer

    answer = max(answer, len(visited))

    for i in range(len(dgs)):
        a, b = dgs[i]
        if is_valid(hp, dgs[i]) and i not in visited:
            dfs(hp-b, dgs, visited | {i})


def solution(k, dungeons):
    global answer
    answer = -1

    dfs(k, dungeons, set())

    return answer
