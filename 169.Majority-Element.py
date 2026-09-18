class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = 0
        count = 0

        for num in nums:
            if count == 0:
                element = num
            if num == element:
                count += 1
            else:
                count -= 1
        
        return element