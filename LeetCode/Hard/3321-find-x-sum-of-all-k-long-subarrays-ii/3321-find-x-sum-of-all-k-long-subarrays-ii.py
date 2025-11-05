from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = Counter()
        A = SortedList()
        B = SortedList()
        A_sum = 0
        out = []

        def rebalance():
            nonlocal A_sum
            while len(A) < x and B:
                f, v = B.pop()
                A.add((f, v))
                A_sum += f * v
            while len(A) > x:
                f, v = A.pop(0)
                A_sum -= f * v
                B.add((f, v))
            while B and A and B[-1] > A[0]:
                f1, v1 = B.pop()
                f2, v2 = A.pop(0)
                A_sum += f1 * v1 - f2 * v2
                A.add((f1, v1))
                B.add((f2, v2))

        def insert_val(num):
            nonlocal A_sum
            old = (cnt[num], num)
            if old in A:
                A.remove(old)
                A_sum -= old[0] * old[1]
            elif old in B:
                B.remove(old)
            cnt[num] += 1
            new = (cnt[num], num)
            B.add(new)
            rebalance()

        def delete_val(num):
            nonlocal A_sum
            old = (cnt[num], num)
            if old in A:
                A.remove(old)
                A_sum -= old[0] * old[1]
            else:
                B.remove(old)
            cnt[num] -= 1
            if cnt[num] > 0:
                B.add((cnt[num], num))
            else:
                del cnt[num]
            rebalance()

        for i in range(k):
            insert_val(nums[i])
        out.append(A_sum)

        for i in range(k, len(nums)):
            delete_val(nums[i - k])
            insert_val(nums[i])
            out.append(A_sum)

        return out