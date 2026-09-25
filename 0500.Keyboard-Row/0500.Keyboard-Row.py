from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        op = []

        for word in words:
            if all(char in r1 for char in word.lower()):
                op.append(word)
            elif all(char in r2 for char in word.lower()):
                op.append(word)
            elif all(char in r3 for char in word.lower()):
                op.append(word)
        
        return op


# print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))  # Output: ['Alaska', 'Dad']
# print(Solution().findWords(["Hello", "BMX", "QWERTY"]))  # Output: ['BMX', 'QWERTY']