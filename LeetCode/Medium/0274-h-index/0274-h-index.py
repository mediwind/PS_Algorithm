class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        
        number = citations[0]
        cnt = 0
        answer = [0]
        for cit in citations:
            if number != cit:
                number = cit
            
            cnt += 1
            if number > 0 and cnt >= number:
                answer.append(min(cnt, number))
        
        if len(citations) == 1 and number:
            return 1
        return max(answer)