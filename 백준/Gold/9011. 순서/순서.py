import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())  # 순열의 크기
    R = list(map(int, input().strip().split()))  # 주어진 R 배열

    # 결과를 저장할 S 배열
    S = [0 for _ in range(n)]
    available = list(range(1, n + 1))  # 1부터 n까지의 숫자 리스트

    possible = True
    for i in range(n - 1, -1, -1):  # 뒤에서부터 처리
        if R[i] >= len(available):
            possible = False
            break
        S[i] = available.pop(R[i])  # R[i]에 해당하는 위치의 숫자를 S[i]에 배치

    if possible:
        print(" ".join(map(str, S)))
    else:
        print("IMPOSSIBLE")