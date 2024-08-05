from itertools import combinations


def calculation(recipe):
    soreness, bitterness = 1, 0
    for s, b in recipe:
        soreness *= s
        bitterness += b
    return abs(soreness - bitterness)


n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
for i in range(1, n + 1):
    for combi in combinations(ingredients, i):
        tmp = calculation(combi)
        ans = min(ans, tmp)

print(ans)