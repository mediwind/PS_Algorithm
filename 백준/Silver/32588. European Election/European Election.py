import sys
input = sys.stdin.readline


def beats(a, b, positions, num_ballots):
    """
    반환값: 후보 a가 후보 b와의 1대1 대결에서 더 많은 표를 얻으면 True
    positions[i][c] = i번째 유권자가 후보 c를 선호 순위에서 몇 번째에 놓았는지
    """
    count_a = 0
    count_b = 0
    for i in range(num_ballots):
        pa = positions[i][a]
        pb = positions[i][b]
        if pa < pb:
            count_a += 1
        elif pb < pa:
            count_b += 1
    return count_a > count_b


n, k = map(int, input().split())

# positions[i][c]: i번째 투표에서 후보 c의 순위 (작을수록 선호)
positions = [[0] * (k + 1) for _ in range(n)]

# 각 투표를 한 줄씩 읽기
for i in range(n):
    line = input().split()
    v = int(line[0])  # 선호하는 후보의 수
    prefs = list(map(int, line[1:]))  # 선호 순위
    # 선호 순위 기록
    for rank, cand in enumerate(prefs):
        positions[i][cand] = rank
    # 언급되지 않은 후보들은 rank = v (동일 순위)
    for cand in range(1, k + 1):
        if positions[i][cand] == 0 and (v == 0 or cand not in prefs):
            positions[i][cand] = v

# 후보 d를 임의로 1번으로 시작
d = 1
# 단계별로 더 강한 후보가 있으면 d에 갱신
for cand in range(2, k + 1):
    if beats(cand, d, positions, n):
        d = cand

# d가 모든 후보를 이기는지 최종 확인
for cand in range(1, k + 1):
    if cand == d:
        continue
    if not beats(d, cand, positions, n):
        print("impossible")
        break
else:
    print(d)