import sys
input = sys.stdin.readline

n = int(input())
strengths = []

for _ in range(n):
    strengths.append(int(input()))

strengths.sort(reverse=True)

if n == 0:
    print(0)
else:
    stable_count = 1
    stable_sum = strengths[0]
    
    candidate_count = 0
    candidate_sum = 0
    
    for i in range(1, n):
        strength = strengths[i]
        
        candidate_count += 1
        candidate_sum += strength
        
        if candidate_sum >= stable_sum:
            stable_count += candidate_count
            stable_sum += candidate_sum
            
            candidate_count = 0
            candidate_sum = 0
    
    print(stable_count)