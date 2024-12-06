def is_possible(A, N, K, min_diff):
    count = 1
    last = A[0]
    for i in range(1, N):
        if A[i] - last >= min_diff:
            count += 1
            last = A[i]
        if count >= K:
            return True
    return False


def max_subset_value(N, K, A):
    A.sort()
    left, right = 0, A[-1] - A[0]
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        if is_possible(A, N, K, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer


N, K = map(int, input().split())
A = list(map(int, input().split()))


print(max_subset_value(N, K, A))