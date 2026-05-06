import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    s = int(input().rstrip())
    ans = 0
    # k^2이 s보다 크거나 같아지는 최초의 순간(최소 크기) 찾기
    while ans * ans < s:
        ans += 1
        
    print(ans)