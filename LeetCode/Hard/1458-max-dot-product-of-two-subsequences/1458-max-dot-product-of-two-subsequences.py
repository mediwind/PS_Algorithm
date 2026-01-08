class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}

        def compute_max_product(index_a, index_b):
            if index_a == len(nums1) or index_b == len(nums2):
                return float("-inf")

            if (index_a, index_b) in cache:
                return cache[(index_a, index_b)]

            current_product = nums1[index_a] * nums2[index_b]

            best_value = max(
                current_product + compute_max_product(index_a + 1, index_b + 1),
                current_product,
                compute_max_product(index_a + 1, index_b),
                compute_max_product(index_a, index_b + 1),
            )

            cache[(index_a, index_b)] = best_value
            return best_value

        return compute_max_product(0, 0) 