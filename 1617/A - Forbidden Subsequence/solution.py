import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().strip()
    t_str = input().strip()
    
    count = [0] * 26
    for char in s:
        count[ord(char) - ord('a')] += 1
        
    if t_str == "abc" and count[0] > 0 and count[1] > 0 and count[2] > 0:
        ans = []
        ans.append('a' * count[0])
        ans.append('c' * count[2])
        ans.append('b' * count[1])
        for i in range(3, 26):
            if count[i] > 0:
                ans.append(chr(i + ord('a')) * count[i])
        print("".join(ans))
        
    else:
        print("".join(sorted(s)))