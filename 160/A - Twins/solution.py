import sys
input = sys.stdin.readline
 
n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
 
total_sum = sum(coins)
my_sum = 0
count = 0
 
for coin in coins:
    my_sum += coin
    count += 1
    if my_sum > total_sum - my_sum:
        break
 
print(count)