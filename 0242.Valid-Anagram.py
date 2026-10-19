class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(s)
        b = set(t)

        if len(s) != len(t):
            return False
        
        if a.issubset(b):
            for ch in a:
                if s.count(ch) != t.count(ch):
                    return False
            return True
        
        return False

# print(Solution().isAnagram("anagram","nagaram")) #True
# print(Solution().isAnagram("-++-","++--")) #True
# print(Solution().isAnagram("flamingo","mango")) #False
# print(Solution().isAnagram("a","ab")) #False