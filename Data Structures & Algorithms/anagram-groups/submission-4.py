class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sorting(s):
            return ''.join(sorted(s))

        sorted_strs = []
        for x in strs:
            sorted_strs.append(sorting(x))

        seen = {}
        for i in range(len(strs)):
            if sorted_strs[i] in seen:
                seen[sorted_strs[i]].append(strs[i])

            else:
                seen[sorted_strs[i]] = [strs[i]]

        res = []

        for x in seen.values():
            res.append(x)

        return res
        
            