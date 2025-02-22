#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in "AEIOUaeiou"]
        results = [i if i not in "AEIOUaeiou" else vowels.pop() for i in s]
        return "".join(results)
# @lc code=end

