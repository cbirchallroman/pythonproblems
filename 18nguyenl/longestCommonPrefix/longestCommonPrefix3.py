from typing import List

strs = ["flower","flow","flight"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) <= 0):
            return ""
        if (len(strs) == 1):
            return strs[0]
        cmp = min(strs, key=len)

        prefix_length = len(cmp)

        for s in strs:
            j = 0
            while (j < prefix_length and cmp[j] == s[j]):
                j += 1
            prefix_length = j
        return cmp[:prefix_length]


print(Solution().longestCommonPrefix(strs))
