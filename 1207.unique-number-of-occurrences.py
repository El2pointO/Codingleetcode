#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
'''

Given an array of integers arr, return true if the number 
of occurrences of each value in the array is unique or false otherwise.
'''
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dicti  = {}
        for nums in arr:
            dicti[nums] = dicti.get(nums,0) + 1

        return len(set(dicti.values())) == len(dicti.values())
# @lc code=end

