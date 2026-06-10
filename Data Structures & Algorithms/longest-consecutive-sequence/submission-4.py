class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        seq = 0
        for num in nums:
            if (num-1) not  in numSet:
                longest = 0
                while (num+longest) in numSet:
                    longest += 1
                    seq = max(seq,longest)

        return seq