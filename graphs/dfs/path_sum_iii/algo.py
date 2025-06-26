from typing import Optional
from utils.debug import CallTracker

tracker = CallTracker()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def path_sum(root: Optional[TreeNode], target_sum: int) -> int:
    # @tracker.track
    def dfs(node: Optional[TreeNode], total: int) -> int:
        if not node:
            return 0

        count = 0
        sum_path = total + node.val
        # dfs path sum equals the target sum
        if sum_path == target_sum:
            count += 1

        # and count all paths that continue their path sum to equal target_sum
        count += dfs(node.left, sum_path) + dfs(node.right, sum_path)

        # and count all paths where nodes left or right starts with total = 0
        count += dfs(node.left, 0) + dfs(node.right, 0)

        return count

    return dfs(root, 0)
