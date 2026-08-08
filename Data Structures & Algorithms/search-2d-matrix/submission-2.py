class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            if matrix[row][-1] <target:
                continue
            else:
                l, r = 0, n-1
                while l<=r:
                    mid = (l+r)//2
                    if target<matrix[row][mid]:
                        r = mid - 1
                    elif target > matrix[row][mid]:
                        l = mid + 1
                    else: return True
                break
                # return False
        return False

