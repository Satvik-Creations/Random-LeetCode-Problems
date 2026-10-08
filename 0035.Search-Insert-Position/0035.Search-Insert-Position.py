from typing import List

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = (low + high) // 2
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
        return low

# print(Solution().searchInsert([1,3,5,6], 5)) #2
# print(Solution().searchInsert([1,3,5,6], 2)) #1
# print(Solution().searchInsert([1,3,5,6], 7)) #4
# print(Solution().searchInsert([1,3,5,6], 0)) #0