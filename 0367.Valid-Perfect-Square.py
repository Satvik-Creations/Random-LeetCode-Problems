class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
            
        low = 0
        high = num-1

        while (low <= high):
            mid  = (low + high)//2

            if (mid*mid == num):
                return True
            elif (num < mid*mid):
                high = mid - 1
            else:
                low = mid + 1

        return False