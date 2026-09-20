class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    Pcopy = p.copy()
                    Pcopy.insert(i, num)
                    new_perms.append(Pcopy)

            perms = new_perms

        return perms