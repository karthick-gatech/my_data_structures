# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

import sys

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.length_of_lis(nums, -sys.maxint, 0)

    def length_of_lis(self, nums, prev, curpos):
        if curpos == len(nums):
            return 0

        taken = 0
        if nums[curpos] > prev:
            taken = 1 + self.length_of_lis(nums, nums[curpos], curpos + 1)
        nottaken = self.length_of_lis(nums, prev, curpos + 1)
        return max(taken, nottaken)