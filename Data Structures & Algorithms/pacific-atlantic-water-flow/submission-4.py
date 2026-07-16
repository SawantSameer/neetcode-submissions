class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dx, dy in directions:
                dfs(r + dx, c + dy, visited, heights[r][c])

        pac_visited = set()
        atl_visited = set()

        for c in range(COLS):
            dfs(0, c, pac_visited, heights[0][c])
            dfs(ROWS - 1, c, atl_visited, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac_visited, heights[r][0])
            dfs(r, COLS - 1, atl_visited, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac_visited and (r, c) in atl_visited:
                    res.append([r, c])

        return res
