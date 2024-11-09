def count_patties(level, number):
    if level == 0:
        return 1
    if number == 1:
        return 0
    elif number == burger[level - 1] + 1:
        return patties[level - 1]
    elif number < burger[level - 1] + 1:
        return count_patties(level - 1, number - 1)
    elif number == burger[level - 1] + 2:
        return patties[level - 1] + 1
    elif number <= burger[level - 1] * 2 + 2:
        return patties[level - 1] + 1 + count_patties(level - 1, number - burger[level - 1] - 2)
    else:
        return patties[level - 1] * 2 + 1


n, x = map(int, input().split())
patties = [0] * 51
bread = [0] * 51
burger = [0] * 51

patties[0] = 1
bread[0] = 0
burger[0] = patties[0] + bread[0]

for i in range(1, n + 1):
    patties[i] = patties[i - 1] * 2 + 1
    bread[i] = bread[i - 1] * 2 + 2
    burger[i] = patties[i] + bread[i]

print(count_patties(n, x))