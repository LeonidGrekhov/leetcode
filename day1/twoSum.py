from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()  # Create a set to store previously seen numbers
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement of the current number
            if complement in num_set:
                # If complement found, return the indices
                # Note that we can directly get the index of the complement from the set
                return [nums.index(complement), i]
            num_set.add(num)  # Add the number to the set
        return [] 