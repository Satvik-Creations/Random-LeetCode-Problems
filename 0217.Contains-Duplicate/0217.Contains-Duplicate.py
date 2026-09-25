from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

# print(Solution().containsDuplicate([1,2,3,4,5,6,7,8,9,10])) #False
# print(Solution().containsDuplicate([2,14,18,22,22])) #True