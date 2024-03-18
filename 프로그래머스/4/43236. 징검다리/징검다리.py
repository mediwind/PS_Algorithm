def solution(distance, rocks, n):
    rocks.sort()
    rocks = rocks + [distance]
    
    lt, rt = 0, distance
    answer = 0
    
    while lt <= rt:
        mid = (lt + rt) // 2
        minimum_distance = float('inf')
        now = 0
        cnt = 0
        
        for rock in rocks:
            diff = rock - now
            if mid > diff:
                cnt += 1
            else:
                minimum_distance = min(minimum_distance, diff)
                now = rock
        
        if cnt > n:
            rt = mid - 1
        else:
            answer = minimum_distance
            lt = mid + 1
    
    return answer