from typing import List


# Not much of a dp algorithm, but more of a greedy one
# since we can decrement the number of steps from the largest
# number at either the offset or at the current position
#
# ie
#  2  1  0
#     3  2  1  0  select 3 because 3 >= 1
#        1  0     continue from 3 since 2 >= 1
#           1  0  continue from 3 since 1 >= 1
# [2, 3, 1, 1, 4]
def can_jump(nums: List[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True

    steps = nums[0]

    for i in range(n - 1):
        steps -= 1
        if steps < 0:
            return False
        steps = max(steps, nums[i + 1])

    return steps >= 0
