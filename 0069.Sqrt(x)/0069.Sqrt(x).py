class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0
        high = x

        while (low <= high):
            mid = (low + high)//2
            if (mid*mid == x):
                return mid
                break
            elif (x < mid*mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return high


# print(Solution().mySqrt(4)) #2
# print(Solution().mySqrt(8)) #2
# print(Solution().mySqrt(75)) #8
