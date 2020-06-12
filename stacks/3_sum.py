# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# [-1,0,1,2,-1,-4]
# ans
#   [-1, 0, 1], [-1, -1, 2]


def threeSum(self, nums):
    nums.sort()
    N, result = len(nums), []
    for i in range(N):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = nums[i] * -1
        s, e = i + 1, N - 1
        while s < e:
            if nums[s] + nums[e] == target:
                result.append([nums[i], nums[s], nums[e]])
                s = s + 1
                while s < e and nums[s] == nums[s - 1]:
                    s = s + 1
            elif nums[s] + nums[e] < target:
                s = s + 1
            else:
                e = e - 1
    return result