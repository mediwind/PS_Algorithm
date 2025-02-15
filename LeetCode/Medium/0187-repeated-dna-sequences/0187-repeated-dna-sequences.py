class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return list()
            
        seen = set()
        ans = set()
        
        # 첫 윈도우는 미리 처리
        curr = s[:10]
        seen.add(curr)
        
        # 슬라이딩 윈도우
        for i in range(1, len(s) - 9):
            # 새 윈도우는 이전 윈도우에서 첫 문자를 제거하고 새 문자를 추가
            curr = curr[1:] + s[i + 9]
            
            if curr in seen:
                ans.add(curr)
            else:
                seen.add(curr)
                
        return list(ans)