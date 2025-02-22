#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]  # Padding to avoid edge cases
        count = 0
        i = 1  # Start from index 1 because of padding

        while i < len(flowerbed) - 1:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 1  # Skip next index

            if count >= n:
                return True
            i += 1

        return count >= n  
# @lc code=end

