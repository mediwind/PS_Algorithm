class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {value: index for index, value in enumerate(arr2)}
        
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))