class Solution:

    def __init__(self, nums: List[int]):
        """
        Initializes the object with the original array.
        Stores both the original array and a copy to be shuffled.
        """
        self.original = list(nums) # Store a copy of the original array
        self.current = list(nums)  # Store a working copy for shuffling

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration.
        """
        self.current = list(self.original) # Restore from the original copy
        return self.current

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array using the Fisher-Yates algorithm.
        """
        random.shuffle(self.current) # Shuffle the working copy in-place
        return self.current
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()