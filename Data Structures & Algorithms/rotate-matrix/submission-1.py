class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix)==1:return matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        l, r = 0, len(matrix)-1
        while l<r:
            for i in range(len(matrix)):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l,r = l+1, r-1
        
