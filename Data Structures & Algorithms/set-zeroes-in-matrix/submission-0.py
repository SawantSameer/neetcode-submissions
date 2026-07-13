class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        target_idx = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    target_idx.append([i,j])

        for row, cols in target_idx:
            for c in range(len(matrix[0])):
                matrix[row][c] = 0
            for r in range(len(matrix)):
                matrix[r][cols] = 0


    
        