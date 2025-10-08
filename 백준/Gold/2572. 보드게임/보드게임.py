import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def solve():
    n = int(input().rstrip())
    card_colors = input().rstrip().split()
    m, k = map(int, input().rstrip().split())
    
    adj = [[] for _ in range(m + 1)]
    for _ in range(k):
        u, v, color = input().split()
        u, v = int(u), int(v)
        adj[u].append((v, color))
        adj[v].append((u, color))
    
    dp = {}
    
    def dfs(node, card_index):
        if (node, card_index) in dp:
            return dp[(node, card_index)]
        
        if card_index == n:
            return 0
        
        max_score = 0
        for neighbor, color in adj[node]:
            score = 0
            if card_colors[card_index] == color:
                score = 10
            
            max_score = max(max_score, score + dfs(neighbor, card_index + 1))
        
        dp[(node, card_index)] = max_score
        return max_score
    
    print(dfs(1, 0))

solve()