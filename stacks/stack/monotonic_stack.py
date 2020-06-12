t = [2, 9, 7, 8, 3, 4, 6, 1]

# getPLE(t)
# [1, 1, 2, 1, 4, 1, 1, 8]
# getNLE(t)
# [7, 1, 2, 1, 3, 2, 1, 1]

def getPLE(nums):
    n = len(nums)
    left, monstack = [-1] * n, []
    for i in range(n):
        while monstack and nums[i] < nums[monstack[-1]]:
            monstack.pop()
        left[i] = monstack[-1] if monstack else -1
        monstack.append(i)
    for i in range(n):
        left[i] = i+1 if left[i] == -1 else i - left[i]
    return left


def getNLE(nums):
    n = len(nums)
    right, monstack = [-1] * n, []
    for i in range(n):
        while monstack and nums[i] < nums[monstack[-1]]:
            print 'Contents of monstack: {}'.format(monstack)
            right[monstack.pop()] = i
        monstack.append(i)
        print 'Contents of monstack after append: {}'.format(monstack)
    print right
    for i in range(n):
        right[i] = n - i if right[i] == -1 else right[i] - i
    return right


mod = (10 ** 9) + 7
left = getPLE(t)
right = getNLE(t)

print sum(a * l * r for a, l, r in zip(t, left, right)) % mod
