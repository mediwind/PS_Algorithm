def find_last_ride(N, M, ride_times):
    # 이분 탐색을 위한 초기 설정
    left, right = 0, N * max(ride_times)
    
    while left < right:
        mid = (left + right) // 2
        total_rides = M  # 모든 놀이기구가 처음에 한 번씩 탑승 가능
        
        for time in ride_times:
            total_rides += mid // time
        
        if total_rides >= N:
            right = mid
        else:
            left = mid + 1
    
    # 마지막 아이가 탑승할 시간을 찾음
    last_time = left
    total_rides = M
    
    for time in ride_times:
        total_rides += (last_time - 1) // time
    
    # 마지막 아이가 탑승할 놀이기구 번호 찾기
    for i in range(M):
        if last_time % ride_times[i] == 0:
            total_rides += 1
        if total_rides == N:
            return i + 1

# 입력 처리
N, M = map(int, input().split())
ride_times = list(map(int, input().split()))

# 결과 출력
print(find_last_ride(N, M, ride_times))