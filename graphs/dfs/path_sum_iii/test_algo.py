import pytest
from typing import Optional, List
from .algo import TreeNode, path_sum

@pytest.mark.parametrize("root, target_sum, expected", [
    ([5,2,None,1], 8, 1),
    ([10,5,-3,3,2,None,11,3,-2,None,1], 8, 3),
    ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22, 3),
])
def test_path_sum(root, target_sum, expected):
    tree = build_tree(root)
    assert path_sum(tree, target_sum) == expected

def build_tree(root: List[Optional[int]]) -> Optional[TreeNode]:
    if not root:
        return None
    root_node = TreeNode(root[0])
    queue = [root_node]
    i = 1
    while queue and i < len(root):
        node = queue.pop(0)
        if root[i] is not None:
            node.left = TreeNode(root[i])
            queue.append(node.left)
        i += 1
        if i < len(root) and root[i] is not None:
            node.right = TreeNode(root[i])
            queue.append(node.right)
        i += 1
    return root_node

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
