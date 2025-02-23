#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
'''
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum,window_sum)
        
        return max_sum / k
            
# @lc code=end