import sys
input = sys.stdin.readline

def calculate_winning_time(num_contestants, intervals):
    start, end = 0, 100_000

    while start <= end:
        mid = (start + end) / 2
        flag = False
        winning_probability = 1

        for interval_start, interval_end, interval_length in intervals:
            if mid > interval_end:
                flag = True
                break
            if mid < interval_start:
                continue
            winning_probability *= (interval_end - mid) / interval_length  # 한 사람에 대해 이기는 확률

        if flag:
            end = mid
            continue

        if abs(winning_probability - 0.5) < 0.00000001:
            break
        if winning_probability > 0.5:
            start = mid
        else:
            end = mid

    return start


num_contestants = int(input())
intervals = []
for _ in range(num_contestants):
    start, end = map(float, input().rstrip().split())
    intervals.append((start, end, end - start))

result = calculate_winning_time(num_contestants, intervals)
print(result)