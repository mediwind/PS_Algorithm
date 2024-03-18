n, c = map(int, input().split())
arr = list(map(int, input().split()))
frequency = dict()

for number in arr:
    frequency[number] = frequency.get(number, 0) + 1

ans = ''
for number in sorted(frequency, key = lambda x: -frequency[x]):
    ans += f'{number} ' * frequency[number]
print(ans.strip())