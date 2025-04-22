class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Case 1: Assume original[0] = 0
        original = [0]
        for i in range(len(derived)):
            original.append(original[-1] ^ derived[i])
        if original[0] == original[-1]:
            return True

        # Case 2: Assume original[0] = 1
        original = [1]
        for i in range(len(derived)):
            original.append(original[-1] ^ derived[i])
        if original[0] == original[-1]:
            return True

        return False