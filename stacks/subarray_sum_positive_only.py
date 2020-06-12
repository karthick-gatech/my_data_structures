# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum >= s.
# If there isn't one, return 0 instead.

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.


def minimum_length_subarray_positive(list1, s):
    n = len(list1)
    ans = n + 1
    left, sum = 0, 0
    for i in range(n):
        sum = sum + list1[i]
        while sum >= s:
            ans = min(ans, i+1-left)
            sum = sum - list1[left]
            left = left + 1
    if ans == n + 1:
        return 0
    else:
        return ans


s = 8
nums = [1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2]
print minimum_length_subarray_positive(nums, s)

s = 4
nums = [3, -2, 5]
print minimum_length_subarray_positive(nums, s)
