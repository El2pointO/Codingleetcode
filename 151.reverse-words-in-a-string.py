#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        str_splt = str.split(s)
        rev_str = str_splt[::-1]
        return " ".join(rev_str)
        
# @lc code=end

