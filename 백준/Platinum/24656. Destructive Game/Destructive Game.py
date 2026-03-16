import sys
input = sys.stdin.readline

n = int(input())
xor_sum = 0

for _ in range(n):
    a, b = map(int, input().split())
    
    if b % 2 != 0:
        # b가 홀수인 경우
        g = a % 2
    else:
        # b가 짝수인 경우
        rem = a % (b + 1)
        if rem == b:
            g = 2
        else:
            g = rem % 2
            
    # 각 무더기의 Grundy 값을 XOR 연산
    xor_sum ^= g

# 최종 XOR 합이 0보다 크면 선공(Alice) 승리, 0이면 후공(Bob) 승리
if xor_sum > 0:
    print("Alice")
else:
    print("Bob")