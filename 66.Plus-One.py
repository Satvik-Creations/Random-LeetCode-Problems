from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst = []
        strnum = ""
        for i in (digits):
            strnum += str(i)
        intnump1 = int(strnum) + 1
        intnump1 = str(intnump1)
        intnump1 = intnump1.replace(""," ")
        intnump1 = intnump1.strip()
        intnump1 = intnump1.split(" ")

        for j in intnump1:
            lst.append(int(j))
        return lst


# print(Solution().plusOne([1,2,3]))
# print(Solution().plusOne([4,3,9,9]))