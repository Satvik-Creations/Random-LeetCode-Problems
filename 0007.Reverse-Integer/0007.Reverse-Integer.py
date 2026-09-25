class Solution:
    def reverse(self, x: int) -> int:
        if x not in range(-2**31, 2**31 - 1):
            return 0
        else:
            y = str(x)
            if y.startswith("-"):
                ans = int(f"-{y[::-1][:-1]}")
            else:
                ans = int(y[::-1])
            
            if -(2**31) <= ans <= 2**31 - 1:
                return ans
        return 0


# print(Solution().reverse(-1234)) #-4321
# print(Solution().reverse(121)) #121
# print(Solution().reverse(1331)) #1331
# print(Solution().reverse(-14641)) #-14641
# print(Solution().reverse(-12345678)) #-87654321