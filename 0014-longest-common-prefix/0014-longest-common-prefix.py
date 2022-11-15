class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Approach 2
        strs = sorted(strs, key = len)
        common = strs[0]
        for string in range(1, len(strs)):
            if len(strs[string]) < len(common):
                common = str(common[0:len(strs[string])])
            for i in range(0, min(len(strs[string]), len(common))):
                if strs[string][i] == common[i]:
                    continue
                else:
                    common = str(common[0:i])
                    break
        return common
        
        
        # # Approach 1: Brute force
        # common = strs[0]
        # for string in range(1, len(strs)):
        #     if len(strs[string]) < len(common):
        #         common = str(common[0:len(strs[string])])
        #     for i in range(0, min(len(strs[string]), len(common))):
        #         if strs[string][i] == common[i]:
        #             continue
        #         else:
        #             common = str(common[0:i])
        #             break
        # return common
        