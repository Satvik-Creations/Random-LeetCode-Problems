class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        i = -1
        while (4**(i+1) <= n):
            i += 1
            if (n == 4**i):
                return True
        return False