from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        x = nums.count(val)

        for i in range(x):
            nums.remove(val)
        
        # return nums
        return l-x

# print(Solution().removeElement([3,2,2,3], 3))  # Output: 2
# print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))  # Output: 5
