class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [
                 (-1, 0),
            (0,-1),     (0,1),
                  (1,0)
        ]

        def dfs(i,j):
            visited.add((i,j))
            for dr, dc in directions:
                nr, nc = i+dr, j+dc

                if (0<=nr<rows and 0<=nc<cols and
                    grid[nr][nc]=="1" and 
                    (nr, nc) not in visited):
                    dfs(nr, nc)


        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    islands += 1
                    dfs(i,j)

        return islands

