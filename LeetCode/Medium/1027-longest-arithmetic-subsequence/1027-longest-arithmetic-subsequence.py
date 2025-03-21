class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        defaultdict = collections.defaultdict

        n = len(nums)
        if  n <= 2:
            return n
        
        # dy[i]는 nums[i]를 마지막 원소로 하는 등차 부분 수열의 정보를 저장
        dy = [defaultdict(int) for _ in range(n)]
        max_length = 2 # 최소 길이는 2 (두 원소로 이루어진 등차 수열)

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j] # 공차 계산

                # dp[j][diff]가 존재하면 이어서 확장, 없으면 초기화
                if dy[j][diff]:
                    dy[i][diff] = dy[j][diff] + 1
                else:
                    dy[i][diff] = 2

                max_length = max(max_length, dy[i][diff])

        return max_length