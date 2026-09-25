class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.istitle():
            return True
        elif word.islower():
            return True
        elif word.isupper():
            return True
        else:
            return False

# print(Solution().detectCapitalUse("INDIA"))
# print(Solution().detectCapitalUse("leetcode"))
# print(Solution().detectCapitalUse("flaG"))