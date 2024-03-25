class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = list()
        k = 0
        for v in nums:
            if v != val:
                tmp.append(v)
                k += 1
        tmp.sort()
        nums[:] = tmp[:]
        print('nums:', nums)
        print('k', k)
        return k