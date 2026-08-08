import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        s = s.translate(str.maketrans("","",string.punctuation))
        strg = "".join(s.split())

        if strg == strg[::-1]:
            return True
        else:
            return False

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))