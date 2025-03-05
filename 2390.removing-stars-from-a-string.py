#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#
'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
'''
# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s :
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
# @lc code=end

