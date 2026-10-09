"""
Solutuion 1

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
            
# print(Solution().lengthOfLastWord("LeetCode is love")) #4
# print(Solution().lengthOfLastWord("Hello World")) #5

"""
Solution 2

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        word = words[-1]
        l = len(word)
        return l

# print(Solution().lengthOfLastWord("LeetCode is love")) #4
# print(Solution().lengthOfLastWord("Hello World")) #5

