t = int(input().strip())
for _ in range(t):
    s = input().strip()
    k = int(input().strip())
    n = len(s)
    
    solution = []
    
    def backtrack(index, parts, used_parts):
        global solution
        
        # 이미 해를 찾았으면 더 이상 탐색하지 않음
        if solution:
            return
        
        # k개의 부분을 찾았을 때
        if len(parts) == k:
            # 문자열 전체를 사용했다면 성공
            if index == n:
                solution = list(parts)
            return
        
        # 남은 문자열이 남은 부분의 개수보다 적으면 불가능
        if n - index < k - len(parts):
            return
        
        # 다음 부분을 만들기 위해 가능한 모든 길이를 시도
        for end in range(index, n):
            new_part = s[index:end+1]
            
            # 새로운 부분이 기존 부분들과 중복되지 않는 경우
            if new_part not in used_parts:
                parts.append(new_part)
                used_parts.add(new_part)
                backtrack(end+1, parts, used_parts)
                parts.pop()
                used_parts.remove(new_part)
    
    backtrack(0, [], set())
    
    if solution:
        print("YES")
        for part in solution:
            print(part)
    else:
        print("NO")