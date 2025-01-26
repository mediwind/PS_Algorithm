class Solution:
    def reverse(self, x: int) -> int:
        # Check if the number is negative
        negative = x < 0
        # Convert the number to a string and reverse it
        reversed_str = str(abs(x))[::-1]
        # Convert the reversed string back to an integer
        reversed_int = int(reversed_str)
        # If the original number was negative, make the reversed integer negative
        if negative:
            reversed_int = -reversed_int
        # Check if the reversed integer is within the 32-bit signed integer range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int