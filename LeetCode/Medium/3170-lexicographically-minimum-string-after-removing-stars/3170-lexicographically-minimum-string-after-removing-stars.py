class Solution:
    def clearStars(self, s: str) -> str:
        defaultdict = collections.defaultdict

        stack = list()
        pos = defaultdict(list)
        removed = set()
        
        for idx, char in enumerate(s):
            if char == '*':
                for i in range(97, 122 + 1):
                    c = chr(i)
                    if pos[c]:
                        idx_to_remove = pos[c].pop()
                        removed.add(idx_to_remove)
                        break
            else:
                stack.append((idx, char))
                pos[char].append(idx)
        
        ans = ''
        for idx, char in stack:
            if idx not in removed:
                ans += char
        
        return ans
