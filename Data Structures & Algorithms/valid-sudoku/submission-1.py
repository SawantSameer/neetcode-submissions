class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j]!=".": seen.add(board[i][j])

        # column check
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                if board[j][i]!="." :seen.add(board[j][i])

        # grid check
        for k in range(1,4):
            seen = set()
            for i in range(3*(k-1),3*k):
                for j in range(3):
                    if board[i][j] in seen:
                        return False
                    if board[i][j]!=".": seen.add(board[i][j])
            seen = set()
            for i in range(3*(k-1),3*k):
                for j in range(3,6):
                    if board[i][j] in seen:
                        return False
                    if board[i][j]!=".": seen.add(board[i][j])
            seen = set()
            for i in range(3*(k-1),3*k):
                
                for j in range(6,9):
                    if board[i][j] in seen:
                        return False
                    if board[i][j]!=".": seen.add(board[i][j])

        return True

        
                