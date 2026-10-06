class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        for x in strs:
            anagram.append("".join(sorted(x)))

        mapp = dict()
        for i,s in enumerate(anagram):
            if s in mapp:
                mapp[s].append(strs[i])
            else:
                mapp[s] = [strs[i]]

        return list(mapp.values())