# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]

# binary indexed tree
# https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a

nums = [5,2,6,1]
rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
BITree = [0] * (N + 1)

def update(i):
    while i <= N:
        BITree[i] += 1
        i += (i & -i)

def getSum(i):
    s = 0
    while i:
        s += BITree[i]
        i -= (i & -i)
    return s


for x in reversed(nums):
    res += getSum(rank[x] - 1),
    update(rank[x])

print res[::-1]
