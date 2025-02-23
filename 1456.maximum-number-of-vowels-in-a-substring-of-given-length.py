#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#
'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

'''
# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = sum(1 for i in s[:k] if i in vowels)
        max_vowel = count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -=1
            if s[i] in vowels:
                count +=1
            max_vowel = max(max_vowel, count)
        return max_vowel
# @lc code=end

