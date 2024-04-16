n = int(input())
shuffle = list(map(int, input().split()))
shuffle = [i - 1 for i in shuffle]
ids = list(map(int, input().split()))

before = list(range(n))
after = [0 for _ in range(n)]
for _ in range(3):
    for i in range(n):
        after[shuffle[i]] = before[i]
    before[:] = after

res = sorted(list(zip(ids, after)), key = lambda x: x[1])
for r in res:
    print(r[0])