cows = {
    'Mildred': 0,
    'Elsie': 1,
    'Bessie': 2
}
output = [7, 7, 7]

n = int(input())
measure = list()
for _ in range(n):
    a, b, c = input().split()
    measure.append((int(a), b, int(c)))
measure.sort(key = lambda x: x[0])

best = list()
for a, b, c in measure:
    output[cows[b]] += c
    best.append(output.copy())
# best

ans = list()
for b in best:
    tmp = list()
    maxi = max(b)
    for i in range(3):
        if b[i] == maxi:
            tmp.append(i)
    ans.append(tmp)
# ans
cnt = 0
for i in range(1, len(ans)):
    if ans[i-1] != ans[i]:
        cnt+=1
print(cnt + 1)