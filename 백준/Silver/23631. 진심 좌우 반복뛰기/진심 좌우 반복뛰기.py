import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    target_dist = N - 1

    # 근의 공식을 이용해 꽉 채운 구간의 수(m)를 구함
    # m(m+1)/2 * K <= target_dist
    # m^2 + m - 2*target/K <= 0
    discriminant = 1 + 8 * target_dist / K
    m = int((-1 + discriminant**0.5) / 2)

    # m번 구간까지 뛰었을 때의 누적 거리
    current_sum_dist = m * (m + 1) // 2 * K

    # 남은 거리
    rem = target_dist - current_sum_dist

    # m이 짝수: 왼쪽으로 이동하며 끝남 -> 현재 위치 음수, 다음 방향 오른쪽
    if m % 2 == 0:
        # m=0 -> 0, m=2 -> -K, m=4 -> -2K ... 규칙: -(m//2)*K
        current_pos = -(m // 2) * K
        direction = 'R'
        final_pos = current_pos + rem

    # m이 홀수: 오른쪽으로 이동하며 끝남 -> 현재 위치 양수, 다음 방향 왼쪽
    else:
        # m=1 -> K, m=3 -> 2K ... 규칙: ((m+1)//2)*K
        current_pos = ((m + 1) // 2) * K
        direction = 'L'
        final_pos = current_pos - rem

    print(f"{final_pos} {direction}")