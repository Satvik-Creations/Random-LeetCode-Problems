class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = set(sentence)

        p = {'z', 'p', 'i', 'r', 'd', 'o', 'e', 'f', 's', 'b', 'l', 'g', 'v', 't', 'y', 'a', 'j', 'u', 'q', 'n', 'c', 'x', 'w', 'm', 'h', 'k'}

        return (p.issubset(x) == True)


print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(Solution().checkIfPangram("oneofthebestthingsaboutthisdudeisthathecodesverywell"))