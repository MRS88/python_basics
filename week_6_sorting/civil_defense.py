def srt(tupl):
    return tupl[1]


def makeTupl(city, lst):
    b = []
    for i in range(city):
        b.append((i, lst[i]))
    return b


settle = makeTupl(int(input()), list(map(int, input().split())))
shelter = makeTupl(int(input()), list(map(int, input().split())))

settle.sort(key=srt)
shelter.sort(key=srt)

nearest = [None] * len(settle)
s = b = 0
while s < len(settle):
    if b == len(shelter) - 1:
        nearest[settle[s][0]] = shelter[b][0] + 1
        s += 1
    elif abs(settle[s][1] - shelter[b][1]) < \
            abs(settle[s][1] - shelter[b + 1][1]):
        nearest[settle[s][0]] = shelter[b][0] + 1
        s += 1
    else:
        b += 1
print(*nearest)
