n, k = map(int, input().split())
arr = list(map(int, input().split()))

# {0: 1}로 초기화하는 이유는 누적합이 정확히 k가 되는 경우를 처리하기 위함
prefix_sum = {0: 1}
sum_till_now = 0
answer = 0

for num in arr:
    sum_till_now += num
    
    if sum_till_now - k in prefix_sum.keys():
        answer += prefix_sum[sum_till_now - k]
    
    prefix_sum[sum_till_now] = prefix_sum.get(sum_till_now, 0) + 1

print(answer)