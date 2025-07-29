from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def path_sum(root: Optional[TreeNode], target_sum: int) -> int:
    def count_paths(node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0

        sum_path = current_sum + node.val

        count = (sum_path == target_sum) & 1

        count += count_paths(node.left, sum_path)
        count += count_paths(node.right, sum_path)

        return count

    def dfs(node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0

        sum_path = current_sum + node.val

        count = (sum_path == target_sum) & 1

        # explore continuing paths through left and right children
        count += dfs(node.left, sum_path)
        count += dfs(node.right, sum_path)

        # additionally, branch out new sub solutions starting from children
        count += count_paths(node.left, 0)
        count += count_paths(node.right, 0)

        return count

    return dfs(root, 0)


# TODO: optimise algorithm
def path_sum_optimised(root: Optional[TreeNode], target_sum: int) -> int:
    lookup = defaultdict(int)
    lookup[target_sum] = 1

    def count_paths(node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0

        sum_path = current_sum + node.val

        count = (sum_path == target_sum) & 1

        count += count_paths(node.left, sum_path)
        count += count_paths(node.right, sum_path)

        return count

    def dfs(node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0

        sum_path = current_sum + node.val

        count = (sum_path == target_sum) & 1

        # explore continuing paths through left and right children
        count += dfs(node.left, sum_path)
        count += dfs(node.right, sum_path)

        # additionally, branch out new sub solutions starting from children
        count += count_paths(node.left, 0)
        count += count_paths(node.right, 0)

        return count

    return dfs(root, 0)
