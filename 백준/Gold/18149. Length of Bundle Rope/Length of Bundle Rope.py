import heapq
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    packages = list(map(int, input().rstrip().split()))

    heapq.heapify(packages)

    total_rope_length = 0

    # 힙에 패키지가 1개 남을 때까지 반복
    while len(packages) > 1:
        # 가장 작은 두 패키지 크기 꺼내기
        package1 = heapq.heappop(packages)
        package2 = heapq.heappop(packages)

        # 두 패키지 크기 더하기
        current_rope_length = package1 + package2

        # 전체 로프 길이에 더하기
        total_rope_length += current_rope_length

        # 두 패키지 크기의 합을 다시 힙에 넣기
        heapq.heappush(packages, current_rope_length)

    print(total_rope_length)