class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found = haystack.find(needle)
        return found

# print(Solution().strStr("Hello World", "World"))
# print(Solution().strStr("Pneumonoultramicroscopicsilicovolcanoconiosis", "silicovolcanoconiosis"))