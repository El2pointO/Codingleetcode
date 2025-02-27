#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

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

