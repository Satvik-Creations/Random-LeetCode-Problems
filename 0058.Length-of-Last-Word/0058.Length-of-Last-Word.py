class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        word = words[-1]
        l = len(word)
        return l
            
# print(Solution().lengthOfLastWord("LeetCode is love"))