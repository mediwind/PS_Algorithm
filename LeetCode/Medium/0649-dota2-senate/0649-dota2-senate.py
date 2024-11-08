class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radi = deque()
        dire = deque()

        for i in range(n):
            if senate[i] == 'R':
                radi.append(i)
            else:
                dire.append(i)
        

        index = n
        while radi and dire:
            if radi[0] < dire[0]:
                dire.popleft()
                radi.popleft()
                radi.append(n)
            else:
                radi.popleft()
                dire.popleft()
                dire.append(n)
            n += 1

        return "Radiant" if radi else "Dire"