from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        nums[:] = [x for x in nums if x!=0] + [0] * count

# print(Solution().moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]