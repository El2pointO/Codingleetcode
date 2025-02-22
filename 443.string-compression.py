#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0: return 0
        read_c = 0
        write_c = 0
        while read_c < n :
            x = chars[read_c] 
            counter = 0
            while read_c < n and chars[read_c] == x:
                    counter +=1
                    read_c+=1
            chars[write_c] = x
            write_c +=1
            if counter > 1:
                 for d in str(counter):
                      chars[write_c] = d
                      write_c +=1
        return write_c
                


# @lc code=end

