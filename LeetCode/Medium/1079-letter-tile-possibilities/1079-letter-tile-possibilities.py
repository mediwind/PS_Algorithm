class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        words = set()
        for i in range(1, n + 1):
            for perm in itertools.permutations(tiles, i):
                word = ''.join(perm)
                words.add(word)
        
        return len(words)