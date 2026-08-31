class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        marks = set()

        directions = [  [0,-1],
                [-1, 0],        [1,0]
                        ,[0,1]]
        
        def dfs(i,j):
            marks.add((i,j))

            for dr, dc in directions:
                nr, nc = i+dr, j+dc

                if (0<=nr<rows) and (0<=nc<cols) and (nr,nc) not in marks and grid[nr][nc]=="1":
                    dfs(nr, nc)

        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in marks:
                    islands+=1
                    dfs(i,j)

        return islands
