import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.Q = list()  # 최소 힙을 저장할 리스트
        self.ch = set()  # 힙에 있는 요소를 추적할 집합
        self.next_smallest = 1  # 힙이 비어 있을 때 다음으로 작은 정수를 추적할 변수

    def popSmallest(self) -> int:
        if self.Q:
            # 힙이 비어 있지 않으면 가장 작은 요소를 반환
            tmp = heapq.heappop(self.Q)
            self.ch.discard(tmp)
            return tmp
        else:
            # 힙이 비어 있으면 next_smallest를 반환하고 증가시킴
            self.next_smallest += 1
            return self.next_smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.next_smallest and num not in self.ch:
            # num이 next_smallest보다 작고 힙에 없는 경우에만 추가
            self.ch.add(num)
            heapq.heappush(self.Q, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)