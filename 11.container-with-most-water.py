#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
'''
You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
'''
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0  # Left pointer
        right = len(height) - 1  # Right pointer
        max_area = 0

        while left < right:
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# @lc code=end

