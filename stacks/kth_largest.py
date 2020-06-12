from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums:
            return -1
        h = []
        for i in xrange(len(nums)):
            if len(h) < k:
                heappush(h, nums[i])
            else:
                if h[0] < nums[i]:
                    heappop(h)
                    heappush(h, nums[i])
        return h[0]

s = Solution()
print s.findKthLargest([7,10,4,3,20,15], 8)