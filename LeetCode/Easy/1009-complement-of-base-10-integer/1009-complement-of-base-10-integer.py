class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        binary_str = bin(n)[2:]
        complement_str = ""
        for char in binary_str:
            if char == "1":
                complement_str += "0"
            else:
                complement_str += "1"

        return int(complement_str, 2)