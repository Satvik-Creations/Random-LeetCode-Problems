class Solution:
    def isUgly(self, n: int) -> bool:

        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            if n == 2:
                        return True
            if n % 2 == 0:
                return False
        
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
                    
            return True

        factors = []

        if n <= 0:
            return False
        if n == 1:
            return True

        temp = n
        
        for i in range(2, int(temp ** 0.5) + 1):
            if n%i == 0 and is_prime(i):
                factors.append(i)

                while temp % i == 0:
                    temp //= i
        
        if temp > 1:
            factors.append(temp)

        for factor in factors:
            if factor not in {2,3,5}:
                return False
        return True


# print(Solution().isUgly(6))  # True
# print(Solution().isUgly(8))  # True
# print(Solution().isUgly(14))  # False
# print(Solution().isUgly(1))  # True