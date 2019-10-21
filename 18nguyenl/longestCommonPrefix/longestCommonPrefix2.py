from typing import List

strs = ["flower","flow","flight"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) <= 0):
            return ""
        if (len(strs) == 1):
            return strs[0]
        if (len(strs) == 2):
            cmp = strs[0]
            for i in range(1, len(strs)):
                j = 0
                while (j < min(len(cmp), len(strs[i])) and cmp[j] == strs[i][j]):
                    j += 1
            return cmp[:j]
        else:
            return self.longestCommonPrefix(
                [self.longestCommonPrefix(strs[:(len(strs) // 2) + 1]),
                 self.longestCommonPrefix(strs[(len(strs) // 2) + 1:])])


print(Solution().longestCommonPrefix(strs))