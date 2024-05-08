# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    global full_hp
    full_hp = health

    attack_times = [a[0] for a in attacks]
    damage = {a[0]: a[1] for a in attacks}
    cont = 0

    for t in range(1, attacks[-1][0] + 1):
        if t in attack_times:
            health -= damage[t]
            cont = 0
        else:
            health = add_health(health, bandage)
            cont += 1

            if cont == bandage[0]:
                health += bandage[2]
                if health > full_hp:
                    health = full_hp
                cont = 0

        if health <= 0:
            return -1

    return health


def add_health(health, bandage):
    global full_hp
    health += bandage[1]

    if health > full_hp:
        return full_hp

    return health