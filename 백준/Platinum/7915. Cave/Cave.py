import sys
input = sys.stdin.readline

# 1. 입력 처리
n_str = input().strip()
if not n_str:
    sys.exit(0)
n = int(n_str)

# parent 배열 1-indexed (노드 2부터 n까지의 부모 정보)
parent = [0, 0] + [int(input()) for _ in range(n - 1)]

# 2. 서브트리 크기 계산
# 부모 노드의 번호가 자식보다 항상 작으므로 뒤에서부터 O(N)으로 누적 가능
sz = [1] * (n + 1)
for i in range(n, 1, -1):
    sz[parent[i]] += sz[i]

# 3. 각 서브트리 크기의 등장 횟수 카운트
cnt = [0] * (n + 1)
for i in range(1, n + 1):
    cnt[sz[i]] += 1

ans = []
# 4. 약수를 돌며 분할 가능 여부 판별
# k는 나누고자 하는 그룹의 수
for k in range(1, n + 1):
    # k가 n의 약수일 때만 k개의 그룹으로 동일하게 분할 가능
    if n % k == 0:
        s = n // k  # 각 그룹의 노드 개수
        
        # 서브트리 크기가 s의 배수인 노드의 개수를 모두 합산
        multiples_count = 0
        for m in range(s, n + 1, s):
            multiples_count += cnt[m]
            
        # s의 배수인 노드가 정확히 k개라면 k개의 그룹으로 분할 가능
        if multiples_count == k:
            ans.append(k)

# 오름차순으로 출력
print(" ".join(map(str, ans)))