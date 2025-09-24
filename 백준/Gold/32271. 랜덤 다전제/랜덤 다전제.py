import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    W = input().strip()
    
    # 누적 합 계산 (문자열을 두 번 이어붙여 원형 처리)
    pref_A = [0] * (2 * N + 1)
    for i in range(2 * N):
        pref_A[i + 1] = pref_A[i] + (1 if W[i % N] == 'A' else 0)

    total_games = 0
    for _ in range(M):
        s, g = map(int, input().split())
        s -= 1
        wins_needed = (g + 1) // 2
        
        low, high = wins_needed, g
        ans = g
        
        while low <= high:
            L = (low + high) // 2
            
            alice_wins = pref_A[s + L] - pref_A[s]
            bert_wins = L - alice_wins
            
            if alice_wins >= wins_needed or bert_wins >= wins_needed:
                ans = L
                high = L - 1
            else:
                low = L + 1
        total_games += ans
        
    print(total_games)

T = int(input())
for _ in range(T):
    solve()