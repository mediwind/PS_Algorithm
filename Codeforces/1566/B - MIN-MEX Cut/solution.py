import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().rstrip()
    
    zero_blocks = 0
    in_block = False
    
    for char in s:
        if char == '0':
            if not in_block:
                zero_blocks += 1
                in_block = True
        else:
            in_block = False
    
    if zero_blocks == 0:
        print(0)
    elif zero_blocks == 1:
        print(1)
    else:
        print(2)