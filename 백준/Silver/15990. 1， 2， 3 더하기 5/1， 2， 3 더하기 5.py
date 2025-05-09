import sys
input = sys.stdin.readline

MOD = 1_000_000_009

t = int(input())
nums = [int(input()) for _ in range(t)]

max_num = max(nums)
# dy[i][j]는 숫자 i를 1, 2, 3의 합으로 나타내는 방법의 수 중, 마지막 숫자가 j인 경우의 수를 저장
dy = [[0 for _ in range(4)] for _ in range(max_num + 1)]

dy[1][1] = 1 # 1을 1로 표현
dy[2][2] = 1 # 2를 2로 표현
dy[3][1] = dy[3][2] = dy[3][3] = 1 # 3을 나타낼 때 마지막 숫자가 1, 2, 3일 수 있는 경우의 수는 각각 1개씩

for i in range(4, max_num + 1):
    dy[i][1] = (dy[i - 1][2] + dy[i - 1][3]) % MOD
    dy[i][2] = (dy[i - 2][1] + dy[i - 2][3]) % MOD
    dy[i][3] = (dy[i - 3][1] + dy[i - 3][2]) % MOD

for num in nums:
    res = sum(dy[num][1:]) % MOD
    print(res)