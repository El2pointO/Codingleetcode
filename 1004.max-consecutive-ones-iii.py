#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
'''
Given a binary array nums and an integer k, return the maximum number 
of consecutive 1's in the array if you can flip at most k 0's.

Example 

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        max_leng = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k :
                if nums[left] == 0:
                    zero_count -=1
                left +=1
            max_leng = max(max_leng, right - left + 1)
        return max_leng
# @lc code=end

