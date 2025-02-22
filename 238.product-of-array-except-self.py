#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = 1 
        result =[1] * n

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1 
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
# @lc code=end

