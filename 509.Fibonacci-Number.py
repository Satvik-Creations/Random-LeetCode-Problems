class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        
        a = 1
        b = 2

        for i in range(4, n+1):
            c = a + b
            a = b
            b = c
    
        return b

# print(Solution().fib(0)) #0
# print(Solution().fib(1)) #1
# print(Solution().fib(2)) #1
# print(Solution().fib(3)) #2
# print(Solution().fib(7)) #13
# print(Solution().fib(10)) #55
# print(Solution().fib(11)) #89
# print(Solution().fib(12)) #144