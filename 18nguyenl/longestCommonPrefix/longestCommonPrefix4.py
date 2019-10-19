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

        for i in range(prefix_length):
            count = 0
            for s in strs:
                if s[:len(cmp)] == cmp:
                    count += 1
            if count == len(strs):
                return cmp
            else:
                cmp = cmp[:-1]
        return cmp


print(Solution().longestCommonPrefix(strs))
