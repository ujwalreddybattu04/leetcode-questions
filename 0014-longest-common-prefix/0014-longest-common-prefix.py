class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        m=len(strs[0])
        store=""
        for i in range(m):
            if strs[0][i] != strs[len(strs) - 1][i]: 
                break
            else:
                store+=strs[0][i]
        return store        


       

        