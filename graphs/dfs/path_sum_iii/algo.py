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
    def dfs(node: Optional[TreeNode], residual: int) -> int:
        if not node:
            return 0

        total_paths = 0
        remaining = residual - node.val
        # dfs path sum equals the target sum
        if remaining == 0:
            total_paths += 1
        else:
            # sum all paths that are continue to reduce residual down to zero
            total_paths += dfs(node.left, remaining) + dfs(node.right, remaining)

        # and include all paths where nodes left or right starts with residual == target_sum
        total_paths += dfs(node.left, target_sum) + dfs(node.right, target_sum)

        return total_paths

    return dfs(root, target_sum)
