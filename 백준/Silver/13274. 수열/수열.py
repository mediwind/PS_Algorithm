import sys
input = sys.stdin.readline

N, K = map(int, input().split())

sequence = list(map(int, input().split()))

queries = [list(map(int, input().split())) for _ in range(K)]

# 쿼리 처리
for L, R, X in queries:
    # 수열 정렬
    sequence.sort()
    # L부터 R까지 X를 더함 (1-based index를 0-based로 변환)
    for i in range(L-1, R):
        sequence[i] += X

sequence.sort()

print(" ".join(map(str, sequence)))