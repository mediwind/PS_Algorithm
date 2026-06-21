import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().rstrip()
    
    # 1. 이미 짝수인 경우 (맨 뒤 숫자가 짝수)
    if int(s[-1]) % 2 == 0:
        print(0)
    
    # 2. 맨 앞 숫자가 짝수인 경우 (전체 뒤집기 1번이면 끝)
    elif int(s[0]) % 2 == 0:
        print(1)
        
    # 3. 맨 앞/뒤는 홀수지만 내부에 짝수가 존재하는 경우
    else:
        has_even = False
        for char in s:
            if int(char) % 2 == 0:
                has_even = True
                break
                
        # 짝수가 단 하나라도 있다면 2번 만에 가능, 없으면 불가능
        if has_even:
            print(2)
        else:
            print(-1)