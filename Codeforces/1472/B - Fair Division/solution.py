import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    total_weight = sum(candies)
    
    # 1. 무게의 합이 홀수라면 무조건 불가능
    if total_weight % 2 != 0:
        print("NO")
    else:
        # 1g짜리와 2g짜리 사탕의 개수를 각각 셉니다.
        count_1 = candies.count(1)
        count_2 = candies.count(2)
        
        # 2. 무게 합은 짝수인데 2g짜리만 홀수 개 있는 특수 예외 처리
        # (1g짜리가 0개이고 2g짜리가 홀수 개이면 똑같이 나눌 수 없음)
        if count_1 == 0 and count_2 % 2 != 0:
            print("NO")
        else:
            print("YES")