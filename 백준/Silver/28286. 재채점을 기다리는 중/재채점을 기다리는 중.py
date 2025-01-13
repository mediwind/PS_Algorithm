from collections import deque


def pull(arr, p):
    a1, a2 = arr[:p], deque(arr[p:])
    a2.rotate(-1)
    a2[-1] = -1
    return a1 + list(a2)


def push(arr, p):
    a1, a2 = arr[:p], deque(arr[p:])
    a2.rotate(1)
    a2[0] = -1
    return a1 + list(a2)


def calculate_max_correct(arr):
    count = 0
    for i in range(N):
        if answer[i] == arr[i]:
            count += 1
    return count


def dfs(n, Arr):
    global result
    count = calculate_max_correct(Arr)

    if count > result:
        result = count

    if n < K:
        for i in range(N):
            dfs(n + 1, pull(Arr, i))
            dfs(n + 1, push(Arr, i))


N, K = map(int, input().split())
answer = list(map(int, input().split()))
OMR = list(map(int, input().split()))

result = 0
dfs(0, OMR)
print(result)