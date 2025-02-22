#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i,j = 0,0
        len1,len2 = len(word1),len(word2)
        while i < len1 or j < len2:
            if i<len1:
                result.append(word1[i])
                i +=1
            if j< len2:
                result.append(word2[j])
                j+=1
        return "".join(result) 
# @lc code=end