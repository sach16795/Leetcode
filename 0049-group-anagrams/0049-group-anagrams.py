class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            if str(sorted(i)) in seen:
                seen[str(sorted(i))].append(i)
            else:
                seen[str(sorted(i))] = [i] 
        return seen.values()
            