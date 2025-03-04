#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#
'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the
resulting array. Return 0 if there is no such subarray.

'''
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        zeros = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == n else ans

# @lc code=end

