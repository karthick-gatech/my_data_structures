

def can_jump_from_position(position, nums):
    if position == len(nums) - 1:
        return True
    furthest_jump = min(position + nums[position], len(nums) - 1)
    for next_position in range(position + 1, furthest_jump + 1, 1):
        if can_jump_from_position(next_position, nums):
            return True
    return False


def can_jump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return can_jump_from_position(0, nums)


nums = [2, 3, 1, 1, 4]
#nums = [3, 2, 1, 0, 4]
#nums = [5, 1, 5, 2]
print can_jump(nums)
