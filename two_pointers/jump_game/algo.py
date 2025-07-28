from typing import List


# can be treated as a greedy solution since there
# is no backtracking required to calculate the largest jump
# from each position in the array
#
# ex
# [2, 3, 1, 1, 4]
# [2]              range = [0]
#    [3, 1]        range = [1, 2]
#          [1, 4]  range = [3, 4]
def can_jump(nums: List[int]) -> bool:
    left = right = 0

    while right < len(nums) - 1:
        next_max_position = max([i + nums[i] for i in range(left, right + 1)])

        if right == next_max_position:
            return False

        left = right + 1
        right = next_max_position

    return True
