import sys
input = sys.stdin.readline

t_str = input()
T = int(t_str.strip())

for case_num in range(1, T + 1):
    line = input().split()
    if not line:
        break
    n = int(line[0])
    a = int(line[1])
    b = int(line[2])
    
    parents = list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        parent = parents[i - 2]
        adj[parent].append(i)
        
    count_a = [1] * (n + 1)
    count_b = [1] * (n + 1)
    
    # 파이썬의 재귀 한계를 피하기 위해 명시적 스택을 사용한 반복적 DFS
    # 튜플 상태: (노드 번호, 방문 상태: 0=진입, 1=퇴출)
    stack = [(1, 0)]
    path = []
    
    while stack:
        u, state = stack.pop()
        
        if state == 0:
            path.append(u)
            stack.append((u, 1))
            
            for v in reversed(adj[u]):
                stack.append((v, 0))
        else:
            path.pop()
            
            if len(path) >= a:
                count_a[path[-a]] += count_a[u]
                
            if len(path) >= b:
                count_b[path[-b]] += count_b[u]
                
    expected_beauty = 0.0
    
    for i in range(1, n + 1):
        prob_a = count_a[i] / n
        prob_b = count_b[i] / n
        
        prob_painted = 1.0 - (1.0 - prob_a) * (1.0 - prob_b)
        expected_beauty += prob_painted
        
    print(f"Case #{case_num}: {expected_beauty:.6f}")