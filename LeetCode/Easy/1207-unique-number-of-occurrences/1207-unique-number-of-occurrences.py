class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        cnt = set()
        for k, v in count.items():
            if v in cnt:
                return False
            cnt.add(v)
        
        return True