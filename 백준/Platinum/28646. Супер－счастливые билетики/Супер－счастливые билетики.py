import sys
input = sys.stdin.readline
MOD = 998244353

# N이 최대 20만이므로 필요한 최대 팩토리얼을 미리 계산 (메모이제이션)
MAX = 600000
fact = [1] * (MAX + 1)
inv = [1] * (MAX + 1)

for i in range(1, MAX + 1):
    fact[i] = (fact[i - 1] * i) % MOD

inv[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX - 1, -1, -1):
    inv[i] = (inv[i + 1] * (i + 1)) % MOD

line = input()
if not line:
    sys.exit()
    
n = int(line)
m = n // 2

# V1과 V4 그룹에 속한 숫자의 개수 (k)
k = (m + 1) // 2
# V2와 V3 그룹에 속한 숫자의 개수 (l)
l = m // 2

# 첫 번째 독립 사건: k개의 숫자 합이 같은 경우의 수 계산
ans1 = 0
if k == 0:
    ans1 = 1
else:
    N = 2 * k
    S = 9 * k
    for j in range(S // 10 + 1):
        if 0 <= j <= N:
            comb1 = fact[N] * inv[j] % MOD * inv[N - j] % MOD
        else:
            comb1 = 0
            
        n2 = S - 10 * j + N - 1
        r2 = N - 1
        if 0 <= r2 <= n2:
            comb2 = fact[n2] * inv[r2] % MOD * inv[n2 - r2] % MOD
        else:
            comb2 = 0
            
        ways = comb1 * comb2 % MOD
        if j % 2 == 1:
            ans1 = (ans1 - ways + MOD) % MOD
        else:
            ans1 = (ans1 + ways) % MOD

# 두 번째 독립 사건: l개의 숫자 합이 같은 경우의 수 계산
ans2 = 0
if l == 0:
    ans2 = 1
else:
    N = 2 * l
    S = 9 * l
    for j in range(S // 10 + 1):
        if 0 <= j <= N:
            comb1 = fact[N] * inv[j] % MOD * inv[N - j] % MOD
        else:
            comb1 = 0
            
        n2 = S - 10 * j + N - 1
        r2 = N - 1
        if 0 <= r2 <= n2:
            comb2 = fact[n2] * inv[r2] % MOD * inv[n2 - r2] % MOD
        else:
            comb2 = 0
            
        ways = comb1 * comb2 % MOD
        if j % 2 == 1:
            ans2 = (ans2 - ways + MOD) % MOD
        else:
            ans2 = (ans2 + ways) % MOD

# 두 사건은 완전히 독립적이므로 곱해주기
ans = (ans1 * ans2) % MOD
print(ans)