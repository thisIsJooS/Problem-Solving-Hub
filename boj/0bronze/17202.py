def _add(a, b):
    return str((int(a)+ int(b)) % 10)


a, b = input(), input()

new_string = ''
while a and b:
    new_string += a[0]
    new_string += b[0]

    a = a[1:]
    b = b[1:]


while len(new_string) > 2:
    length = len(new_string)
    string = ""

    for i in range(length-1):
        string += _add(new_string[i], new_string[i+1])

    new_string = string

print(string)