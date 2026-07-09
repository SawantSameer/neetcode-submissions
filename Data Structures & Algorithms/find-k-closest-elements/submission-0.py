class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [0]*len(arr)
        for i in range(len(arr)):
            closeness = abs(x-arr[i])
            diff[i] = [closeness,i]

        diff.sort()
        res = []
        for i in range(k):
            res.append(arr[diff[i][1]])
        return sorted(res)