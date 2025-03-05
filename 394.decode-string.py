#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test c

'''
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num*10 + int(ch)
            elif ch == '[':
                stack.append((curr_str,curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                last_str , num = stack.pop()
                curr_str =last_str + num *curr_str
            else:
                curr_str += ch
        return curr_str
# @lc code=end

