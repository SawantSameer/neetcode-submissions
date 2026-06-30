class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def bubbleSort(arr):
            n = len(arr)
            for i in range(n-1):
                for j in range(n-1-i):
                    if arr[j]>arr[j+1]:
                        arr[j],arr[j+1] = arr[j+1], arr[j]

        bubbleSort(nums)
        return nums