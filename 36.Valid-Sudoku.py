from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def box(k,l):
            box_ = set()
            for x in range(k,l):
                for y in range(0,3):
                    if board[x][y] != ".":
                        if board[x][y] in box_:
                            return False
                        box_.add(board[x][y])
            box_.clear()
            for x in range(k,l):
                for y in range(3,6):
                    if board[x][y] != ".":
                        if board[x][y] in box_:
                            return False
                        box_.add(board[x][y])
            box_.clear()
            for x in range(k,l):
                for y in range(6,9):
                    if board[x][y] != ".":
                        if board[x][y] in box_:
                            return False
                        box_.add(board[x][y])
            box_.clear()

        hor = set()
        ver = set()
        
        for a in range(0,9):
            hor.clear()
            for b in board[a]:
                if b != ".":
                    if b in hor:
                        return False
                    hor.add(b)
        for c in range(0,9):
            ver.clear()
            for d in range(0,9):
                if board[d][c] != ".":
                    if board[d][c] in ver:
                        return False
                    ver.add(board[d][c])
                    
        for k in range(0,9,3):
                if box(k,k+3) == False:
                    return False
        
        return True


# print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])) #True
# print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])) #False
# print(Solution().isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]])) #False