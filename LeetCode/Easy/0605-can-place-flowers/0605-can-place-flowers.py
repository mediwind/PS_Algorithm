class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the previous plot is empty or it's the first plot
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                # Check if the next plot is empty or it's the last plot
                next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:  # Can place a flower here
                    n -= 1
                    if n == 0:
                        return True
                    flowerbed[i] = 1  # Place the flower
        
        return False