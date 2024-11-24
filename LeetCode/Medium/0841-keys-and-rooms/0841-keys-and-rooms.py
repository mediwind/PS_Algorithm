class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def DFS(num):
            ch[num] = 1
            for k in rooms[num]:
                key[k] = 1
            
            for i in range(n):
                if key[i] and not ch[i]:
                    DFS(i)
            

        n = len(rooms)
        key = [0 for _ in range(n)]
        key[0] = 1
        ch = [0 for _ in range(n)]
        DFS(0)

        for i in range(n):
            if not ch[i]:
                return False
                
        return True