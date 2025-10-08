def solve():
    N = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    U = list(map(int, input().split()))
    D = list(map(int, input().split()))

    for i in range(N):
        if (L[i] == -1) != (R[i] == -1):
            print("NE")
            return
        if L[i] != -1 and L[i] + R[i] >= N:
            print("NE")
            return
       
        if (U[i] == -1) != (D[i] == -1):
            print("NE")
            return
        if U[i] != -1 and U[i] + D[i] >= N:
            print("NE")
            return

    for r in range(N):
        if L[r] != -1:
            c = L[r]
            if U[c] != -1 and r < U[c]:
                print("NE")
                return
            if D[c] != -1 and r >= N - D[c]:
                print("NE")
                return
       
        if R[r] != -1:
            c = N - 1 - R[r]
            if U[c] != -1 and r < U[c]:
                print("NE")
                return
            if D[c] != -1 and r >= N - D[c]:
                print("NE")
                return

    for c in range(N):
        if U[c] != -1:
            r = U[c]
            if L[r] != -1 and c < L[r]:
                print("NE")
                return
            if R[r] != -1 and c >= N - R[r]:
                print("NE")
                return

        if D[c] != -1:
            r = N - 1 - D[c]
            if L[r] != -1 and c < L[r]:
                print("NE")
                return
            if R[r] != -1 and c >= N - R[r]:
                print("NE")
                return

    print("DA")

solve()