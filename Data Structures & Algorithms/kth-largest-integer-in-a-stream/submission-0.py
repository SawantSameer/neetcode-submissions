class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.index = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.val = val
        self.nums.append(self.val)
        self.nums.sort(reverse = True)
        return self.nums[self.index - 1]
    
