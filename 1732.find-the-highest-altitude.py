#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

'''

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr_alt = 0
        
        for g in gain:
            curr_alt += g
            max_alt = max(max_alt, curr_alt)
        
        return max_alt
# @lc code=end

