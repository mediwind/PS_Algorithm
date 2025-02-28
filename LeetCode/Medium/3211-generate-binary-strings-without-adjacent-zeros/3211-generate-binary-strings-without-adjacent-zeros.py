class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ['0', '1']
        valid = ['0', '1']
        
        for _ in range(n - 1):
            new_valid = list()
            for s in valid:
                if s[-1] == '1':
                    new_valid.append(s + '0')
                    new_valid.append(s + '1')
                else:
                    new_valid.append(s + '1')
            valid = new_valid
        
        return valid