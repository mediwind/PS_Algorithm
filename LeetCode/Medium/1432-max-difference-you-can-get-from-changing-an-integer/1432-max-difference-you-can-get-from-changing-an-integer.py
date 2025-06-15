class Solution:
    def maxDiff(self, num: int) -> int:
        string = str(num)

        # 최대값: 9가 아닌 첫 숫자를 9로 모두 바꿈
        for x in string:
            if x != '9':
                a = string.replace(x, '9')
                break
        else:
            a = string
        
        # 최소값: 첫 자리가 1이 아니면 첫 자리를 1로 모두 바꿈
        if string[0] != '1':
            b = string.replace(string[0], '1')
        else:
            # 첫 자리가 1이면, 0/1이 아닌 첫 숫자를 0으로 모두 바꿈
            for x in string[1:]:
                if x != '0' and x != '1':
                    b = string.replace(x, '0')
                    break
            else:
                b = string

        return int(a) - int(b)
