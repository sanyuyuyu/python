b# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-19 19:57:46
class Solution:
    def maxLengthBetweenEqualCharacters (self, s: str) -> int:
        ans = -1
        firstIndex = {}
        for i, c in enumerate(s):
            if c not in firstIndex:
                firstIndex[c] = i 
            else:
                ans = max(ans, i - firstIndex[c] - 1)
        return ans

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idxs = {}
        ans = -1
        for i, c in enumerate(s):
            idxs[c] = idxs[c] if c in idxs else i
            ans = max(ans, i - idxs[c] - 1)
        return ans
