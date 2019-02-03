from collections import deque

# Leetcode 239
class Solution(object):
    def maxSliding(self, nums, k):
        if len(nums) == 0:
            return []
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        result = []
        for i in range(k, len(nums)):
            result.append(nums[q[0]])

            while q and q[0] <= i - k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        result.append(nums[q[0]])
        return result


def main():
    s = Solution()
    print s.maxSliding([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print s.maxSliding([6, 5, 4, 3, 2, 1], 3)


main()
