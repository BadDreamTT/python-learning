"""LeetCode 101. 对称二叉树（简单）

思路：递归比较左右子树是否互为镜像。
      check(a, b)：a 的左对 b 的右、a 的右对 b 的左（交叉比较）。
时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，h 为树高（递归栈）
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode | None) -> bool:
    if root is None:
        return True

    def check(a: TreeNode | None, b: TreeNode | None) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)

    return check(root.left, root.right)


if __name__ == "__main__":
    #      1
    #     / \
    #    2   2
    #   /\   /\
    #  3 4  4 3   → True
    t1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                  TreeNode(2, TreeNode(4), TreeNode(3)))
    assert is_symmetric(t1) is True

    #      1
    #     / \
    #    2   2
    #     \   \
    #     3   3   → False（3 都在右边，不是镜像）
    t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                  TreeNode(2, None, TreeNode(3)))
    assert is_symmetric(t2) is False

    assert is_symmetric(None) is True
    assert is_symmetric(TreeNode(1)) is True
    print("all tests passed")