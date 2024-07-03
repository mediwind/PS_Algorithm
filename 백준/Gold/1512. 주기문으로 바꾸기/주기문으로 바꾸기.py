M = int(input())
S = input()
answer = float('inf')

for l in range(1, M + 1):
    counter = {}
    tempAnswer = 0
    
    for start in range(l):
        total = 0
        for j in range(start, len(S), l):
            counter[S[j]] = counter.get(S[j], 0) + 1
            total += 1
        
        tempAnswer += (total - max(counter.values()))
        counter.clear()  # MLE 방지
    
    answer = min(answer, tempAnswer)

print(answer)