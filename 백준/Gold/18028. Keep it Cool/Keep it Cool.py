import sys
input = sys.stdin.readline

n, m, s, d = map(int, input().split())
cold = list(map(int, input().split()))

# 각 슬롯에 넣을 수 있는 새 소다의 최대 개수
new_cap = [d - cold[i] for i in range(s)]

# 슬롯을 콜드 소다 개수가 적은 순서로 정렬
slots = list(range(s))
slots.sort(key=lambda i: cold[i])

compromised = []  # 새 소다를 넣어 "위험해지는" 슬롯들
total_cap = 0  # 현재까지 넣을 수 있는 새 소다 총합
for i in slots:
    if total_cap >= n:
        break
    compromised.append(i)
    total_cap += new_cap[i]

# 새 소다를 넣지 않은 슬롯에서 남아있는 콜드 소다 총합
untouched = set(range(s)) - set(compromised)
total_cold = sum(cold[i] for i in untouched)
if total_cold < m:
    print("impossible")
    sys.exit(0)

# compromised에 해당하는 슬롯들에 새 소다 할당
assign = [0] * s
remaining = n
# compromised 슬롯 중 마지막 슬롯 제외하고 최대한 채우기
for idx in compromised[:-1]:
    assign[idx] = new_cap[idx]
    remaining -= new_cap[idx]

# 마지막 compromised 슬롯에는 남은 새 소다 할당 (남은 개수가 new_cap[last]보다 작거나 같아야 함)
if compromised:
    last = compromised[-1]
    assign[last] = remaining
    remaining = 0

print(" ".join(str(x) for x in assign))