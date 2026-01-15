class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def longest_consecutive_length(number_set):
            maximum_length = 1
            for value in number_set:
                current_length = 1
                current_value = value
                while current_value + 1 in number_set:
                    current_value += 1
                    current_length += 1
                if current_length > maximum_length:
                    maximum_length = current_length
            return maximum_length

        if not hBars or not vBars:
            return 1

        horizontal_set = set(hBars)
        vertical_set = set(vBars)

        max_horizontal = longest_consecutive_length(horizontal_set)
        max_vertical = longest_consecutive_length(vertical_set)

        side_length = min(max_horizontal, max_vertical) + 1

        return side_length * side_length