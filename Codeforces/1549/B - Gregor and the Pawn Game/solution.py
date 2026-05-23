import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    enemy = list(input().rstrip())
    gregor = list(input().rstrip())
    
    ans = 0
    for i in range(n):
        if gregor[i] == '1':
            
            # 1순위: 왼쪽 대각선 공격 (적 폰이 있어야 함)
            if i > 0 and enemy[i - 1] == '1':
                ans += 1
                enemy[i - 1] = '2'  # 이미 잡은 적 폰임을 표시
                
            # 2순위: 직진 (빈칸이어야 함)
            elif enemy[i] == '0':
                ans += 1
                enemy[i] = '2'  # 내가 차지한 빈칸임을 표시
                
            # 3순위: 오른쪽 대각선 공격 (적 폰이 있어야 함)
            elif i < n - 1 and enemy[i + 1] == '1':
                ans += 1
                enemy[i + 1] = '2'  # 이미 잡은 적 폰임을 표시
                
    print(ans)