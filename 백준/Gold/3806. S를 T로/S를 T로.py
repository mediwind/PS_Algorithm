t = int(input())

for test in range(1, t + 1):
    before = input().strip()
    after = input().strip()

    zero1 = before.count('0')
    one1 = before.count('1')
    zero2 = after.count('0')
    one2 = after.count('1')

    if one1 > one2:
        print(f"Case {test}: -1")
        continue

    add = 0
    map_changes = dict()

    for i in range(len(before)):
        if before[i] == '0' and after[i] == '1' and zero1 > zero2:
            zero1 -= 1
            add += 1
            map_changes[i] = '1'

    rest_one = one2 - one1
    rest_zero = zero2 - zero1

    if rest_zero < 0:
        print(f"Case {test}: -1")
        continue

    comp = list()

    for i in range(len(before)):
        if before[i] == '?':
            if after[i] == '0' and rest_zero > 0:
                rest_zero -= 1
                comp.append('0')
            elif after[i] == '1' and rest_one > 0:
                rest_one -= 1
                comp.append('1')
            else:
                if rest_zero > 0:
                    comp.append('0')
                else:
                    comp.append('1')
            add += 1
        else:
            if i in map_changes:
                comp.append(map_changes[i])
            else:
                comp.append(before[i])

    change = 0
    for i in range(len(comp)):
        if comp[i] != after[i]:
            change += 1

    print(f"Case {test}: {add + (change // 2)}")