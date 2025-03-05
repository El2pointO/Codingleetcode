#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#
'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''
# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)
        count = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            if col in row_count:
                count += row_count[col]
        return count
# @lc code=end

