"""LeetCode 104. 二叉树的最大深度（简单）

思路：递归。最大深度 = max(左子树深度, 右子树深度) + 1；
      空节点深度为 0（递归终点）。
时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，h 为树高（递归栈），最坏 O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1


if __name__ == "__main__":
    #      3
    #     / \
    #    9  20
    #       /  \
    #      15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1
    print("all tests passed")