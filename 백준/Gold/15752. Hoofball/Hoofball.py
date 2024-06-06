def next_cow(idx):
    if idx == 0:
        return idx + 1
    elif idx == N - 1:
        return idx - 1
    else:
        left_distance = arr[idx] - arr[idx - 1]
        right_distance = arr[idx + 1] - arr[idx]
        
        if left_distance <= right_distance:
            return idx - 1
        
        return idx + 1


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
passed = [0] * N

for i in range(N):
    passed[next_cow(i)] += 1
#     print(arr[i], passed)
# arr
# passed

ball = 0
for i in range(N):
    if passed[i] == 0:
        ball += 1
    # i < next_cow(i): 현재 소(i)가 다음 소(next_cow(i))보다 왼쪽에 있어야 합니다. 이는 공이 왼쪽으로만 이동한다는 규칙 때문입니다.
    # next_cow(next_cow(i)) == i: 현재 소가 공을 받는 소(next_cow(i))에게 공을 넘겼을 때, 그 소가 다시 현재 소에게 공을 넘겨야 합니다. 이는 서로 공을 주고받는 상황을 나타냅니다.
    # passed[i] == 1 and passed[next_cow(i)] == 1: 현재 소와 다음 소가 각각 한 번씩만 공을 받았어야 합니다. 이는 서로 공을 주고받는 상황이며, 이외의 다른 소로부터 공을 받지 않았음을 보장합니다.
    if i < next_cow(i) and next_cow(next_cow(i)) == i and passed[i] == 1 and passed[next_cow(i)] == 1:
        ball += 1

print(ball)