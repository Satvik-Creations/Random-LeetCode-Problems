class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (x == 0):
            return 0.0
        if (x == 1):
            return 1.0
        if (n == 0):
            return 1.0
        if (x == -1 and n%2 == 0):
            return 1.0
        if (x == -1 and n%2 !=0):
            return -1.0

        BinForm = n
        ans = 1

        if (n<0):
            x = 1/x
            BinForm = -BinForm

        while (BinForm > 0):
            if (BinForm %2 == 1):
                ans *= x
            
            x = x*x
            BinForm //= 2
        

        return round(ans,5)

