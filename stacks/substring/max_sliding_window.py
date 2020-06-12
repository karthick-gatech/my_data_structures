from collections import deque

# Leetcode 239
# Given an array nums, there is a sliding window of size k which is
# moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window
# moves right by one position. Return the max sliding window.
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            if deq and deq[0] == i - k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output


def main():
    s = Solution()
    print s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print s.maxSlidingWindow([6, 5, 4, 3, 2, 1], 3)


main()
