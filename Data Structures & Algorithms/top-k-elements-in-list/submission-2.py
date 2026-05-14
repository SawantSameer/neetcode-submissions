from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Create buckets: index = frequency, value = list of numbers
        # Example: if '3' appears 2 times, freq_buckets[2] will contain 3
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)
        
        # 3. Iterate backwards from the highest frequency to find top k
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res