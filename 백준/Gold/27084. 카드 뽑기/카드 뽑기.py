MOD = 10**9 + 7
n = int(input())
cards = list(map(int, input().split()))

count_table = {}
for card in cards:
    if card in count_table:
        count_table[card] += 1
    else:
        count_table[card] = 1

answer = 1
for count in count_table.values():
    answer *= (count + 1)
    answer %= MOD

print((answer - 1) % MOD)