

def preorder(idx):
    if idx not in reverse_dict:
        return ''

    s = ''
    s += reverse_dict[idx]
    s += preorder(idx * 2)
    s += preorder(idx * 2 + 1)

    return s


def inorder(idx):
    if idx not in reverse_dict:
        return ''

    s = ''
    s += inorder(idx*2)
    s += reverse_dict[idx]
    s += inorder(idx*2 + 1)

    return s


def postorder(idx):
    if idx not in reverse_dict:
        return ''

    s = ''
    s += postorder(idx*2)
    s += postorder(idx*2 + 1)
    s += reverse_dict[idx]

    return s



n = int(input())

dict = {}
dict['A'] = 1

for _ in range(n):
    a, b, c = input().split()

    if b != '.':
        dict[b] = dict[a] * 2
    if c != '.':
        dict[c] = dict[a] * 2 + 1

reverse_dict = {}
for k, v in dict.items():
    reverse_dict[v] = k


print(preorder(1))
print(inorder(1))
print(postorder(1))