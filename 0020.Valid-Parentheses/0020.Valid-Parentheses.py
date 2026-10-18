"""
Solution 1: 
Stack Approach, General/Preferred way of solving this question!

"""

# Uses Stack Data Structure and a Dictionary based matching for Valid Parenthesis!

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                
                if stack[-1] != matching[bracket]:
                    return False
                stack.pop()
        
        return len(stack) == 0


"""
Solution 2:
Without stack! [Generally not a preferred way of solving this question!]

"""

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