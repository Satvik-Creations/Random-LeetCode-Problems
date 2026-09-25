from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        chindex = dict()
        for i in range(len(s)):
            chindex[indices[i]] = s[i]

        k = dict(sorted(chindex.items(), key=lambda x: x[0]))
        return ''.join(k.values())

# print(Solution().restoreString("codeleet", [4,5,6,7,0,2,1,3])) #leetcode
# print(Solution().restoreString("abc", [0,1,2])) #abc