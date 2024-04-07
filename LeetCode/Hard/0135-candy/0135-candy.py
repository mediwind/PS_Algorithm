from collections import deque

class Solution:
    def candy(self, ratings: List[int]) -> int:
        dx = [-1, 1]

        n = len(ratings)
        candies = [0 for _ in range(n)]
        ch = [0 for _ in range(n)]

        Q = deque()
        minimum = min(ratings)
        for i in range(n):
            if ratings[i] == minimum:
                Q.append(i)
                candies[i] = 1

        while Q:
            x = Q.popleft()
            ch[x] = 1
            for d in range(2):
                xx = x + dx[d]

                if xx < 0 or xx >= n:
                    continue
                
                if not ch[xx]:
                    if ratings[xx] > ratings[x]:
                        candies[xx] = candies[x] + 1
                    elif ratings[xx] == ratings[x]:
                        candies[xx] = 1
                    Q.append(xx)
        
        # print('candies:', candies)
        # print('ch:', ch)
        return sum(candies)