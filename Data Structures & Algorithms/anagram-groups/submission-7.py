class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def Anagram(s1, s2):
            if len(s1)!=len(s2):
                return False
            seen = {}
            for s in s1:
                seen[s] = 1 + seen.get(s,0)

            for s in s2:
                if s not in seen:
                    return False
                seen[s]-=1
            for x in seen.values():
                if x!=0: return False
            return True

        res = []
        used = set()
        for i in range(len(strs)):
            if i not in used:
                res.append([strs[i]])
                used.add(i)
                for j in range(i+1, len(strs)):
                    if j not in used and Anagram(strs[i],strs[j]):
                        res[-1].append(strs[j])
                        used.add(j)

        return res