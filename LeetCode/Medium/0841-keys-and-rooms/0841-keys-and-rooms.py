class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def DFS(room):
            if room not in ch:
                ch.add(room)
                for key in rooms[room]:
                    DFS(key)
        
        ch = set()
        DFS(0)
        return len(ch) == len(rooms)