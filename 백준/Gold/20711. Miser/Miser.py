import sys
input = sys.stdin.readline

n = int(input().rstrip())
last_visit = {}
dp = [0] * (n + 1)
answer = 0

for day in range(1, n + 1):
    data = list(map(int, input().rstrip().split()))
    k = data[0]
    visitors = data[1:]
    
    value = 1
    for person in visitors:
        if person in last_visit:
            prev_day = last_visit[person]
            cand = dp[prev_day] + 1
            
            if cand > value:
                value = cand
                
        last_visit[person] = day
        dp[day] = value
        
        if value > answer:
            answer = value

print(answer)