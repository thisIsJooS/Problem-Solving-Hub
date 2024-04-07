def solution(a, b):
    row = len(a);
    col = len(b[0]);

    answer = [[0] * col for _ in range(row)]

    for r in range(row):
        for c in range(col):
            for k in range(len(b)):
                answer[r][c] += a[r][k] * b[k][c]

    return answer