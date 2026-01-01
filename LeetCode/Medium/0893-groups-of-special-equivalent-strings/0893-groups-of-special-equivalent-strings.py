class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        seen = set()
        for w in words:
            ev = sorted(w[0::2])
            od = sorted(w[1::2])
            seen.add(("".join(ev), "".join(od)))
            
        return len(seen)