import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    
    mini_idx, maxi_idx = arr.index(min(arr)), arr.index(max(arr))
    left, right = min(mini_idx, maxi_idx), max(mini_idx, maxi_idx)
    
    to_left = n - left
    to_right = right + 1
    to_middle = (left + 1) + (n - right)
    
    ans = min(to_left, to_right, to_middle)
    print(ans)