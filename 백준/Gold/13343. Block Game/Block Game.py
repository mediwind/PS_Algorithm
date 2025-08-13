def find_winner(n, m):
    # m이 0이면 현재 플레이어 패배
    if m == 0:
        return False

    # n이 2m보다 크면 현재 플레이어 승리 (여러 선택지가 존재)
    if n > 2 * m:
        return True

    # 다음 플레이어의 결과와 반대
    return not find_winner(max(m, n % m), min(m, n % m))


n, m = map(int, input().split())

# n >= m을 만족하도록 설정
if find_winner(max(n, m), min(n, m)):
    print("win")
else:
    print("lose")