from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            # Create a frequency array for 'a'-'z'
            count = [0] * 26
            for char in s:
                # ord(char) - ord('a') maps 'a'->0, 'b'->1, ..., 'z'->25
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple so it can be a dictionary key
            ans[tuple(count)].append(s)
            
        return list(ans.values())