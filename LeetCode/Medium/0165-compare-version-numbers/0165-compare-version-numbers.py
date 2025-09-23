class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        from itertools import zip_longest
        nums_1 = version1.split('.')
        nums_2 = version2.split('.')

        for num_1, num_2 in zip_longest(nums_1, nums_2, fillvalue = 0):
            num_1, num_2 = int(num_1), int(num_2)
            if num_1 == num_2:
                continue
            elif num_1 < num_2:
                return -1
            else:
                return 1
        
        return 0