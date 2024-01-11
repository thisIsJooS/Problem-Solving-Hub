def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

current_number = 71529782

while True:
    if is_prime(current_number):
        print("첫 번째로 나타나는 소수:", current_number)
        break
    current_number += 1
