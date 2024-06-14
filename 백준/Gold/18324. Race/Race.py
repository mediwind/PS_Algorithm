'''
이 코드는 이진 탐색을 사용하여 Bessie가 k 미터를 달릴 수 있는 최소 시간을 찾습니다. 
이진 탐색의 범위는 1부터 1e9까지이며, 각 단계에서 Bessie의 최대 속도를 mid로 설정하고 그에 따른 최소 시간을 계산합니다. 

이 시간은 Bessie가 mid m/s까지 속도를 높이는 데 필요한 시간, 
mid m/s에서 x m/s까지 속도를 줄이는 데 필요한 추가 시간, 
그리고 남은 거리를 s m/s의 속도로 달리는 데 필요한 시간을 합한 것입니다. 

이 시간을 ans에 저장하고, 이진 탐색을 계속 진행하여 가능한 최소 시간을 찾습니다.
'''

k, n = map(int, input().split())
for _ in range(n):
    x = int(input())
    # lt and rt are the left and right boundaries for binary search
    # s is the maximum speed Bessie can reach
    # ans is the minimum time Bessie needs to run k meters
    lt, rt, s, ans = 1, 10**9, -1, float('inf')
    while lt <= rt:
        # mid is the middle point between lt and rt
        mid = lt + (rt - lt) // 2
        # dist is the distance Bessie can run if she increases her speed by 1 m/s every second until she reaches mid m/s
        dist = mid * (mid + 1) // 2
        # if dist is greater than k, it means Bessie can reach the finish line before her speed reaches mid m/s
        # so we need to decrease the upper boundary rt
        if dist > k:
            rt = mid - 1
            continue
        
        # remain_dist is the remaining distance Bessie needs to run after her speed reaches mid m/s
        remain_dist = k - dist
        # need_time is the additional time Bessie needs to decrease her speed to x m/s
        need_time = max(0, mid - x)
        
        # if mid is less than or equal to x, it means Bessie doesn't need to decrease her speed
        # so dist_for_dec is 0
        # otherwise, dist_for_dec is the distance Bessie can run if she decreases her speed by 1 m/s every second until she reaches x m/s
        if mid <= x:
            dist_for_dec = 0
        else:
            dist_for_dec = (mid + x - 1) * (mid - x) // 2
        
        # if dist_for_dec is greater than remain_dist, it means Bessie can reach the finish line before her speed decreases to x m/s
        # so we need to decrease the upper boundary rt
        if dist_for_dec > remain_dist:
            rt = mid - 1
        else:
            # otherwise, we update s and increase the lower boundary lt
            s = mid
            lt = mid + 1
            # if the remaining distance can be run at a constant speed of s m/s, we update ans
            if (k - dist - dist_for_dec) % mid == 0:
                ans = min(ans, mid + need_time + (k - dist - dist_for_dec) // mid)
            # otherwise, Bessie needs to run for an additional second at a speed of s m/s
            else:
                ans = min(ans, mid + need_time + (k - dist - dist_for_dec) // mid + 1)
    
    # print the minimum time Bessie needs to run k meters
    print(int(ans))