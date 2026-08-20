class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        suffix = [0]*n
        suffix[n-1] = arr[-1]
        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1], arr[i])

        for i in range(n-1):
            arr[i] = suffix[i+1]
        arr[-1] = -1

        return arr