""" 9분-231229
연속된 하나 이상의 숫자를 모두 뒤집는거 가능
"""
s = input()
n = len(s)

first = s[0]
cnt = [1, 0]
flag = True

for c in s:
    if c == first:
        continue
    else:
        first = c
        if flag:
            cnt[1] += 1
        elif not flag:
            cnt[0] += 1

        flag = not flag

print(min(cnt))