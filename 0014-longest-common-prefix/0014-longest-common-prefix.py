class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for string in range(1, len(strs)):
            if len(strs[string]) < len(common):
                common = str(common[0:len(strs[string])])
            for i in range(0, min(len(strs[string]), len(common))):
                print (i)
                print(common)
                print(strs[string])
                if strs[string][i] == common[i]:
                    continue
                else:
                    common = str(common[0:i])
                    break
        return common
        