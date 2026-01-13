class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def compute_area_difference(cut_y: float, square_list: List[List[int]]) -> float:
            area_above = 0.0
            area_below = 0.0

            for square in square_list:
                _, bottom_y, side_length = square
                square_area = side_length * side_length

                if cut_y <= bottom_y:
                    area_above += square_area
                elif cut_y >= bottom_y + side_length:
                    area_below += square_area
                else:
                    height_above = (bottom_y + side_length) - cut_y
                    height_below = cut_y - bottom_y
                    area_above += side_length * height_above
                    area_below += side_length * height_below

            return area_above - area_below

        lower_bound = 0.0
        upper_bound = 2 * 1e9

        for _ in range(60):
            midpoint = (lower_bound + upper_bound) / 2.0
            difference = compute_area_difference(midpoint, squares)

            if difference > 0:
                lower_bound = midpoint
            else:
                upper_bound = midpoint

        return upper_bound