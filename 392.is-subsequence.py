#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



'''
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        write = 0 # pointer for t
        read = 0 # pointer for s
        n, m = len(t), len(s)
        while read < m and write < n :
            if s[read] == t[write]:
                read +=1
            write +=1
        
        return read == m

# @lc code=end

