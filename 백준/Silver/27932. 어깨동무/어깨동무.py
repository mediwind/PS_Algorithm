def count_tired(heights, H):
    n = len(heights)
    tired = 0
    
    for i in range(n):
        left = abs(heights[i] - heights[i-1]) if i > 0 else 0
        right = abs(heights[i] - heights[i+1]) if i < n-1 else 0
        if (i > 0 and left > H) or (i < n-1 and right > H):
            tired += 1
            
    return tired


n, k = map(int, input().split())
heights = list(map(int, input().split()))
left, right = 0, max(abs(heights[i] - heights[i+1]) for i in range(n-1)) if n > 1 else 0

answer = right
while left <= right:
    mid = (left + right) // 2
    tired = count_tired(heights, mid)
    if tired <= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(answer)