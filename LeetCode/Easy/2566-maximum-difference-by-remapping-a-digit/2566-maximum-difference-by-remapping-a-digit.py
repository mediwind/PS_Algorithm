class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # 최대값: num의 각 자릿수 중 하나를 골라 9로 모두 바꾼다
        max_val = num
        for d in set(s):
            if d != '9':
                candidate = int(s.replace(d, '9'))
                if candidate > max_val:
                    max_val = candidate

        # 최소값: num의 각 자릿수 중 하나를 골라 0으로 모두 바꾼다
        min_val = num
        for d in set(s):
            if d != '0':
                candidate = int(s.replace(d, '0'))
                if candidate < min_val:
                    min_val = candidate
                    
        return max_val - min_val