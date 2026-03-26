import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

count_j = 0
count_o = 0
count_i = 0

state_memo = {(0, 0): -1}

max_length = 0

for i in range(n):
    char = s[i]
    
    if char == 'J':
        count_j += 1
    elif char == 'O':
        count_o += 1
    elif char == 'I':
        count_i += 1
        
    state = (count_j - count_o, count_j - count_i)
    
    if state in state_memo:
        length = i - state_memo[state]
        if length > max_length:
            max_length = length
    else:
        state_memo[state] = i

print(max_length)