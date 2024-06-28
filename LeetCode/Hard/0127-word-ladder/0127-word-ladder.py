class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def compare(word, candidate):
            cnt = 0
            for i in range(len(word)):
                if word[i] != candidate[i]:
                    cnt += 1
                if cnt >= 2:
                    return False
            return True
        

        Q = deque()
        Q.append((beginWord, 0))
        visit = {beginWord}
        while Q:
            word, distance = Q.popleft()
            if word == endWord:
                return distance + 1
            for candidate in wordList:
                if candidate not in visit and compare(word, candidate):
                    Q.append((candidate, distance + 1))
                    visit.add(candidate)
        
        return 0