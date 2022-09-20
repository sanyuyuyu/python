# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-20 20:35:26
class Solution:
    def getMaaximumGenrated(self, n: int) -> int:
        if n == 0:
            return 0 
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return max(nums)


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0 :
            return 0
        if n==1 :
            return 1
        nums = [0]*(n+1)
        nums[1]=1
        max = 1
        for i in range(2,n+1):
            nums[i]=nums[i//2]+i%2*nums[i//2+1]
            if max<nums[i]:
                max = nums[i]
        return max
