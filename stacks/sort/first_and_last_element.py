# Given an array of integers nums sorted in ascending order, find the
# starting and ending position of a given target value.
# If the target is not found in the array, return [-1, -1].

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = [-1, -1]
        if len(nums) == 0:
            return output
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) / 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid

        if nums[i] != target:
            return output
        else:
            output[0] = i

        j = len(nums) - 1
        while i < j:
            mid = (i + j) / 2 + 1
            # make mid biased to right for this
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        output[1] = j
        return output