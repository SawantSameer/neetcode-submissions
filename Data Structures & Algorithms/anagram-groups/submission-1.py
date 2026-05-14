from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a key
            key = "".join(sorted(s))
            # defaultdict automatically creates [] if the key is missing
            seen[key].append(s)
            
        return list(seen.values())