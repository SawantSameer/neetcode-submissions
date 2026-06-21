class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        for i in range(r):
            if matrix[i][c-1]<target:
                continue
            else:
                l,r = 0,c-1
                while l<=r:
                    mid = (l+r)//2
                    if matrix[i][mid]<target:
                        l = mid + 1
                    elif matrix[i][mid]>target:
                        r = mid - 1
                    else:
                        return True

        return False