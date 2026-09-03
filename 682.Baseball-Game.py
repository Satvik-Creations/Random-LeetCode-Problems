from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i.isdigit() or (i.startswith("-") and i[1:].isdigit()):
                record.append(int(i))
            else:
                if i=="C":
                    record.remove(record[-1])
                elif i=="D":
                    record.append(2*(record[-1]))
                elif i=="+":
                    sumr = record[-1] + record[-2]
                    record.append(sumr)
        return sum(record)
            

# print(Solution().calPoints(["5","2","C","D","+"])) #30
# print(Solution().calPoints(["5","-2","4","C","D","9","+","+"])) #27

