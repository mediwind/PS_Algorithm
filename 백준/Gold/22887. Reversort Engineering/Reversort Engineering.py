def reverse(L, i, j):
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1


def reversort_engineering(N, C):
    if not (N-1 <= C <= (N+2)*(N-1)//2):
        return "IMPOSSIBLE"
    result = list(range(1, N+1))
    for i in reversed(range(N-1)):
        l = min(C-i, N-i)
        C -= l
        reverse(result, i, i+l-1)
    return " ".join(map(str, result))


T = int(input())
for case in range(T):
    N, C = map(int, input().split())
    result = reversort_engineering(N, C)
    print(f"Case #{case+1}: {result}")