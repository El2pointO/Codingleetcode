#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        read = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[read] = nums[read], nums[i]
                read +=1
        return nums
# @lc code=end

