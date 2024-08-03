class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 10 = 2 * 5
        # In a Factorial of number "x" , Number of 2's will be greater than Number of 5's
        # So, Count of 5's determines, number of Trailing zeroes in a Factorial
        # Q) How to find number of 5's in "x" factorial ?
        # A) Count Number of 5's from 1 to x 
        # x / 5 --> Gives Number of 5 factors until x
        # x / 25 --> Gives Number of 25 factors until x
        # We also have to check for 5^3, 5^4 as they also have extra 5's in them

        ans = 0
        i = 5

        # Make a Loop, until Division between n & i can Happen
        while n // i : # while n / i > 0:
            # Count Number of 5's
            fives_count = n // i  # Floor Division, to get rid of Decimal Part
            ans += fives_count
            i = i * 5  # Multiplying i with 5, to check with further 5 Multiples
        
        return ans