years = {'Ox': 1,
    'Tiger': 2,
    'Rabbit': 3,
    'Dragon': 4,
    'Snake': 5,
    'Horse': 6,
    'Goat': 7,
    'Monkey': 8,
    'Rooster': 9,
    'Dog': 10,
    'Pig': 11,
    'Rat': 12}

birth = {
    'Bessie': ['Ox', 0]
}
N = int(input())
for _ in range(N):
    statement = input().split()
    cow = statement[0]
    born_year = years[statement[4]] # 태어난 연도
    criterion_year = years[birth[statement[-1]][0]] # 비교 연도
    
    if statement[3] == 'previous':
        if born_year >= criterion_year:
            res = -(12 - born_year + criterion_year)
        else:
            res = -(criterion_year - born_year)
    else:
        if born_year <= criterion_year:
            res = 12 - criterion_year + born_year
        else:
            res = born_year - criterion_year

    birth[cow] = [statement[4], birth[statement[-1]][1] + res]

print(abs(birth['Elsie'][1]))