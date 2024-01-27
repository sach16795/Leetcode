class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = []
            for j in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.append(board[i][j]) 
        for j in range(9):
            seen = []
            for i in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.append(board[i][j]) 
        for i in range(3):
            for j in range(3):
                seen = []
                for ii in range(3):
                    for jj in range(3):
                        if board[(i*3) + ii][(j*3) + jj] in seen:
                            return False
                        if board[(i*3) + ii][(j*3) + jj] != ".":
                            seen.append(board[(i*3) + ii][(j*3) + jj]) 
        return True
             