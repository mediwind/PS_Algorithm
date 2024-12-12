from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
friendships = [tuple(map(int, input().split())) for _ in range(M)]

# 그래프를 인접 리스트로 표현
friends = defaultdict(set)
for A, B in friendships:
    friends[A].add(B)
    friends[B].add(A)

min_friend_sum = float("inf")

# 각 사람에 대해 그 사람의 친구들 중에서 두 사람을 선택하여 세 사람의 친구 관계를 확인
for A in range(1, N + 1):
    for B in friends[A]:
        if B > A:  # 중복 계산 방지
            for C in friends[A]:
                if C > B and C in friends[B]:  # 중복 계산 방지 및 세 사람의 친구 관계 확인
                    # 친구 수 계산 (각 사람의 친구 수에서 다른 두 사람을 제외)
                    friend_sum = (len(friends[A]) - 2) + (len(friends[B]) - 2) + (len(friends[C]) - 2)
                    min_friend_sum = min(min_friend_sum, friend_sum)

# 결과 출력
if min_friend_sum == float("inf"):
    print(-1)
else: 
    print(min_friend_sum)