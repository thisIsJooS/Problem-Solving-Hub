s = input()

alpha = []
nums = []

for c in s:
    if ord('A') <= ord(c) <= ord('Z'):
        alpha.append((ord(c), c))
    else:
        nums.append(c)

alpha.sort()
res = ""
for a in alpha:
    res += a[1]
for n in nums:
    res += n

print(res)

"""
K1K5CB7
AJKDLSI412K4JSJ9D
"""