def solution(s):
    length = len(s)
    res = length

    for unit in range(1, length//2 +1):
        prev = s[0:unit]
        compressed = ''; cnt = 1;
        for i in range(unit, length, unit):
            if prev == s[i:i+unit]:
                cnt += 1
            else:
                if cnt == 1:
                    compressed += ''.join(prev)
                else:
                    compressed += str(cnt) + ''.join(prev)
                prev = s[i:i+unit]
                cnt = 1

        if cnt == 1:
            compressed += ''.join(prev)
        else:
            compressed += str(cnt) + ''.join(prev)
        res = min(res, len(compressed))

    return res

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("aabcabcabcabca"))