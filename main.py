color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
[first, second, third] = [input() for _ in range(3)]

f = color.index(first)
s = color.index(second)
t = color.index(third)

res = ''
res += str(f)
res += str(s)

tval = '1' + '0'*t
print(int(res) * int(tval))