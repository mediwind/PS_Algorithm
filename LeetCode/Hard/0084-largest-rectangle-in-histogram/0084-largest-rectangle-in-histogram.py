class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = list()
        
        extended_heights = heights + [0]
        
        for i, h_current in enumerate(extended_heights):
            
            while stack and extended_heights[stack[-1]] > h_current:
                h_popped = extended_heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h_popped * width)
                # print(i, h_popped * width)

            stack.append(i)
            # print(i, stack, max_area)
        return max_area