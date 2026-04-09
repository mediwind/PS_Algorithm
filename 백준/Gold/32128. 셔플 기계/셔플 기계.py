import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 각 셔플 기술의 사이클 분할 정보를 저장할 리스트
shuffle_cycles = []

for _ in range(M):
    S = list(map(int, input().split()))
    inv = [0] * N
    
    # 역순열 생성
    for i in range(N):
        inv[S[i] - 1] = i
        
    # 순열 사이클 분할 수행
    visited = [False] * N
    cycles = []
    
    for i in range(N):
        if not visited[i]:
            cycle = []
            curr = i
            # 순환 고리를 찾을 때까지 추적
            while not visited[curr]:
                visited[curr] = True
                cycle.append(curr)
                curr = inv[curr]
            cycles.append(cycle)
            
    shuffle_cycles.append(cycles)

# 초기 카드 배열
cards = list(range(1, N + 1))

# K번의 셔플 명령 실행
for _ in range(K):
    X, Y = map(int, input().split())
    X -= 1  # 0-indexed 변환
    
    new_cards = [0] * N
    
    # 해당 셔플 기술의 사이클 정보를 순회
    for cycle in shuffle_cycles[X]:
        L = len(cycle)
        # Y가 아무리 커도 O(1)로 이동 거리 압축
        shift = Y % L
        
        # 압축된 이동 거리만큼 한 번에 값을 갱신
        for j in range(L):
            new_cards[cycle[j]] = cards[cycle[(j + shift) % L]]
            
    cards = new_cards

print(*cards)