# I know ofc, this solution is not recommended for interview purposes, I have gone through this approach so as to just test my python deep skills also It's my choice to try different approaches.
# I will definitely improve the solution in future, but for now I am done with it, Temporarily!

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        x = set(nums)
        y = list(x)
        y.sort()

        for i in range(len(y)):
            nums[i] = y[i]
        
        return len(y)

# print(Solution().removeDuplicates([1,1,2]))
# print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))