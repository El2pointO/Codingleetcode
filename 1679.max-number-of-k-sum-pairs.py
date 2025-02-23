#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#
'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
'''
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        nums.sort()
        n = len(nums)
        right = n-1
        while left < right:
            if (nums[left] + nums[right] == k):
                count += 1
                left += 1 
                right -= 1 
            elif nums[left] + nums[right] < k:
                left += 1 
            else:
                right -= 1  
        return count
# @lc code=end

