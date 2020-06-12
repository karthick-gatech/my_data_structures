
class State(object):
    GOOD = 1
    BAD = 2
    UNKNOWN = 3


def can_jump_from_position(position, nums, memo):
    if memo[position] != State.UNKNOWN:
        return True if memo[position] == State.GOOD else False

    furthest_jump = min(position + nums[position], len(nums) - 1)
    for next_position in range(position + 1, furthest_jump + 1, 1):
        if can_jump_from_position(next_position, nums, memo):
            memo[position] = State.GOOD
            return True

    memo[position] = State.BAD
    return False


def can_jump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    memo = []
    for i in range(len(nums)):
        state = State()
        memo.append(state.UNKNOWN)
    memo[len(memo) - 1] = State.GOOD
    print memo
    return can_jump_from_position(0, nums, memo)


# bottom-up
def can_jump_2(nums):
    memo = []
    for i in range(len(nums)):
        state = State()
        memo.append(state.UNKNOWN)
    memo[len(memo) - 1] = State.GOOD
    for i in range(len(nums)-2, -1, -1):
        furthest_jump = min(i + nums[i], len(nums)-1)
        for j in range(i+1, furthest_jump+1, 1):
            if memo[j] == State.GOOD:
                memo[i] = State.GOOD
                break
    return memo[0] == State.GOOD

#nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
#nums = [5, 1, 5, 2]
print can_jump(nums)
print can_jump_2(nums)