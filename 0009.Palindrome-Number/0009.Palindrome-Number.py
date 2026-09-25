class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)

# print(Solution().isPalindrome(121)) #True
# print(Solution().isPalindrome(1331)) #True
# print(Solution().isPalindrome(123)) #False
