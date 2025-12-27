class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            srt_str = "".join(sorted(word))
            if srt_str in seen:
                seen[srt_str].append(word)
            else:
                seen[srt_str] = [word]
        return [value for value in seen.values()]