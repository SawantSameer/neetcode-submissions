class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]

        visit = set()
        def dfs(i,j):
            visit.add((i,j))

            for dr, dc in directions:
                nr, nc = dr+i, dc+j
                if (0<=nr<rows) and (0<=nc<cols) and (nr,nc) not in visit and board[nr][nc]=="O":
                    dfs(nr,nc)

        for r in [0,rows-1]:
            for c in range(cols):
                if board[r][c]=="O":
                    dfs(r,c)

        for c in [0,cols-1]:
            for r in range(rows):
                if board[r][c]=="O":
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit:
                    board[r][c]="X"

                
