class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in t:
            if t.count(x) > s.count(x):
                return x

# print(Solution().findTheDifference("abcd", "abcde"))
# print(Solution().findTheDifference("a", "aa"))