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
def jump(nums: List[int]) -> int:
    jumps = 0
    left = right = 0

    while right < len(nums) - 1:
        max_position = 0
        for i in range(left, right + 1):
            # calculate relative position from the max nums[i]
            max_position = max(max_position, i + nums[i])

        left = right + 1
        right = max_position
        jumps += 1

    return jumps
