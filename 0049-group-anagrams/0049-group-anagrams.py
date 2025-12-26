class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        a = []
        for string in strs: 
            srt = "".join(sorted(string))
            if srt in seen:
                seen[srt].append(string)
            else:
                seen[srt] = [string]
        return [value for value in seen.values()]