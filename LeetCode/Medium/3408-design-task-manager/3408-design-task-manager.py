class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        import heapq
        self._heap = list()
        self._tasks = dict()
        for user_id, task_id, priority in tasks:
            self._tasks[task_id] = (user_id, priority)
            heapq.heappush(self._heap, (-priority, -task_id, task_id))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        import heapq
        self._tasks[taskId] = (userId, priority)
        heapq.heappush(self._heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        import heapq
        user, _ = self._tasks[taskId]
        self._tasks[taskId] = (user, newPriority)
        heapq.heappush(self._heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        
        if taskId in self._tasks:
            del self._tasks[taskId]

    def execTop(self) -> int:
        import heapq
        while self._heap:
            neg_prio, neg_tid, tid = heapq.heappop(self._heap)
            prio = -neg_prio

            info = self._tasks.get(tid)
            if info is None:
                continue
            user, cur_prio = info
            if cur_prio != prio:
                continue

            del self._tasks[tid]
            return user
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()