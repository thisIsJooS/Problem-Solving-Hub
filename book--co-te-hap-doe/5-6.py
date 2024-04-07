def solution(N, stages):
    total = len(stages)
    rates = [0]

    for now in range(1, N + 1):
        count = stages.count(now)

        if total == 0:
            rate = 0
            rates.append(rate)
        else:
            rate = count / total
            rates.append(rate)
            total -= count

    answer = []
    for i, rate in enumerate(rates):
        if i == 0:
            continue

        answer.append((i, rate))

    answer.sort(key=lambda x: x[1], reverse=True)

    answer = [a[0] for a in answer]

    return answer