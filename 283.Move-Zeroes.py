from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0

        for i in nums:
            if i == 0:
                count += 1

        for j in range(count):
            nums.remove(0)

        for k in range(count):
            nums.append(0)

# print(Solution().moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]