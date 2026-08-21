class Solution:
    def isValid(self, s: str) -> bool:
        br1 = "({["
        br2 = ")}]"
        r, c, sq = "()", "{}", "[]"

        for k in range(len(s)):
            for i in br1:
                for j in br2:
                    if f"{i}{j}" in [r, c, sq] and f"{i}{j}" in s:
                        s = s.replace(f"{i}{j}", "")

        return s == ""


# print(Solution().isValid("{[]}")) #True
# print(Solution().isValid("()")) #True
# print(Solution().isValid("{[}]")) #False
# print(Solution().isValid("{[}]}})")) #False