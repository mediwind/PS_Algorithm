import sys
input = sys.stdin.readline

while True:
    A = int(input())
    if not A:
        break
    
    cnt = 0
    for k in range(1, A):
        if not A**2 % k and not (A**2 // k - k) % 2:
            B = (A**2 // k - k) // 2
            if B <= A:
                break
            cnt += 1
    
    print(cnt)