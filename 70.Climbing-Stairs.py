class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        a = 1
        b = 2

        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
    
        return b

# print(Solution().climbStairs(2)) #2
# print(Solution().climbStairs(3)) #3
# print(Solution().climbStairs(7)) #13