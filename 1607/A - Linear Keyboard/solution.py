import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    keyboard = input().rstrip()
    s = input().rstrip()
    
    pos = {}
    for index, char in enumerate(keyboard):
        pos[char] = index
        
    total_time = 0
    for i in range(len(s) - 1):
        current_char = s[i]
        next_char = s[i + 1]
        
        total_time += abs(pos[current_char] - pos[next_char])
        
    print(total_time)