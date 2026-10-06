class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        original = x
        reverse = 0

        while x>0:
            digit = x%10
            reverse = reverse*10 + digit
            x = x//10
        
        return original == reverse

# print(Solution().isPalindrome(121)) #True
# print(Solution().isPalindrome(1331)) #True
# print(Solution().isPalindrome(123)) #False
