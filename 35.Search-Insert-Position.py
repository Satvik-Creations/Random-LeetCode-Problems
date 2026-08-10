from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target > max(nums):
                return nums.index(nums[-1])+1
            elif nums[i] == target:
                return i
            elif nums[i] > target:
                return i

# print(Solution().searchInsert([1,3,5,6], 5)) #2
# print(Solution().searchInsert([1,3,5,6], 2)) #1
# print(Solution().searchInsert([1,3,5,6], 7)) #4
# print(Solution().searchInsert([1,3,5,6], 0)) #0