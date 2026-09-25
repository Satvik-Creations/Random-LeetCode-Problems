class Solution: 
    def isPowerOfTwo(self, n: int) -> bool: 
        if n <= 0: 
            return False
        elif n == 1: 
            return True
        else:
            i = 1

            while 2 ** i <= n:
                if 2 ** i == n:
                    return True
                i += 1

            return False

# print(Solution().isPowerOfTwo(32)) #True
# print(Solution().isPowerOfTwo(64)) #True
# print(Solution().isPowerOfTwo(4096)) #True
# print(Solution().isPowerOfTwo(57167)) #False