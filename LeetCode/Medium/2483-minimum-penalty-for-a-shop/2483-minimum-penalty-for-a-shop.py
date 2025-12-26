class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = customers.count('Y')
        best_pen = penalty
        best_hour = 0
        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < best_pen:
                best_pen = penalty
                best_hour = i + 1
                
        return best_hour