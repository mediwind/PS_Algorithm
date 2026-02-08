import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    curr_c = 2 * A[0] - 1
    C_list = [curr_c]

    for i in range(1, N):
        curr_c = 2 * A[i] - curr_c
        C_list.append(curr_c)

    final_c = C_list[-1]

    if abs(final_c) != 1:
        print("NO")
        continue

    if final_c == 1:
        req_k_parity = N % 2
    else:
        req_k_parity = (N - 1) % 2

    limit_prefix = N
    for i in range(N - 1):
        if C_list[i] < 1:
            limit_prefix = i + 1
            break

    last_violation = 0
    for i in range(N - 1):
        val = C_list[i]
        idx = i + 1

        if idx % 2 == req_k_parity:
            if val < 2:
                last_violation = idx
        else:
            if val < 0:
                last_violation = idx

    found = False
    k = limit_prefix

    if k % 2 == req_k_parity:
        if k > last_violation:
            found = True
    else:
        if k - 1 > last_violation:
            found = True

    if found:
        print("YES")
    else:
        print("NO")