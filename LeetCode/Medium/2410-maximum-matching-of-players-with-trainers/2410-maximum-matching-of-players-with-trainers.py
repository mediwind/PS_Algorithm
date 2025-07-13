class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        ans = 0
        lt, rt = 0, 0
        while lt < len(players) and rt < len(trainers):
            if players[lt] <= trainers[rt]:
                lt += 1
                rt += 1
                ans += 1
            else:
                rt += 1
        
        return ans