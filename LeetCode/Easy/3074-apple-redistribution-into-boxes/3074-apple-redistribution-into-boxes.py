class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse = True)
        s = 0
        for i, c in enumerate(capacity, 1):
            s += c
            if s >= total:
                return i
                
        return len(capacity)