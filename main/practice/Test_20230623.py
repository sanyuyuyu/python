# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) <= 1:
#             return len(nums)
#         dp = [1] * len(nums)
#         result = 1
#         for i in range(1, len(nums)):
#             for j in range(0, i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#             result = max(result, dp[i]) 
#         return result


# def longestCommonPrefix(self, strs):
#         if not strs: return ""
#         ss = list(map(set, zip(*strs)))
#         res = ""
#         for i, x in enumerate(ss):
#             x = list(x)
#             if len(x) > 1:
#                 break
#             res = res + x[0]
#         return res


