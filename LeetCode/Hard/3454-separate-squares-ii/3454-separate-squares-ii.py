class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        sweep_events = []

        for x_coord, y_coord, side_length in squares:
            sweep_events.append((y_coord, 1, x_coord, x_coord + side_length))
            sweep_events.append((y_coord + side_length, -1, x_coord, x_coord + side_length))

        sweep_events.sort()

        active_intervals = []
        previous_y = sweep_events[0][0]
        total_area = 0.0
        area_segments = []

        def merged_interval_length(interval_list):
            interval_list.sort()
            total_length = 0
            current_end = -10**30

            for start, end in interval_list:
                if start > current_end:
                    total_length += end - start
                    current_end = end
                elif end > current_end:
                    total_length += end - current_end
                    current_end = end

            return total_length

        for current_y, event_type, left_x, right_x in sweep_events:
            if current_y > previous_y and active_intervals:
                height = current_y - previous_y
                width = merged_interval_length(active_intervals)
                area_segments.append((previous_y, height, width))
                total_area += height * width

            if event_type == 1:
                active_intervals.append((left_x, right_x))
            else:
                active_intervals.remove((left_x, right_x))

            previous_y = current_y

        half_area = total_area / 2.0
        accumulated_area = 0.0

        for base_y, height, width in area_segments:
            segment_area = height * width
            if accumulated_area + segment_area >= half_area:
                return base_y + (half_area - accumulated_area) / width
            accumulated_area += segment_area

        return 0.0
