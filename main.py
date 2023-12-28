data = ['7 8', '1 2', '1 5', '2 3', '2 6', '3 4', '4 7', '5 6', '6 4']

n, m = data[0].split()
print(n)
print(m)

for e in data[1:]:
    a, b= e.split()
    print(f'a : {a}, b : {b}')


# arr = []
# for _ in range(9):
#     arr.append(input())
#
# print(arr)