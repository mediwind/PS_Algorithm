class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side_length = 0
        rectangle_count = len(bottomLeft)

        for i in range(rectangle_count):
            for j in range(i + 1, rectangle_count):
                overlap_left_x = max(bottomLeft[i][0], bottomLeft[j][0])
                overlap_right_x = min(topRight[i][0], topRight[j][0])
                overlap_bottom_y = max(bottomLeft[i][1], bottomLeft[j][1])
                overlap_top_y = min(topRight[i][1], topRight[j][1])

                if overlap_left_x < overlap_right_x and overlap_bottom_y < overlap_top_y:
                    possible_side = min(
                        overlap_right_x - overlap_left_x,
                        overlap_top_y - overlap_bottom_y,
                    )
                    if possible_side > max_side_length:
                        max_side_length = possible_side

        return max_side_length * max_side_length