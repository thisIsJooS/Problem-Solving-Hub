n = input()
length = len(n)

ll, rr = 0, 0
for i in range(0, length//2):
    ll += int(n[i])
for i in range(length//2, length):
    rr += int(n[i])

if ll == rr:
    print("LUCKY")
else:
    print("READY")