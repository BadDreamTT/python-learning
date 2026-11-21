"""LeetCode 100. 相同的树（简单）

思路：递归同步遍历两棵树，结构不同或值不同即返回 False。
时间复杂度：O(min(m, n))
空间复杂度：O(min(h1, h2))，递归栈
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None and q is None:      # 都空 → 相同
        return True
    if p is None or q is None:       # 一个空 → 不同
        return False
    return (p.val == q.val
            and is_same_tree(p.left, q.left)     # 同侧比较（不是交叉）
            and is_same_tree(p.right, q.right))


if __name__ == "__main__":
    #   1        1
    #  / \      / \
    # 2   3    2   3   → True
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) is True

    #   1        1
    #  /          \
    # 2            2   → False（结构不同）
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p, q) is False

    assert is_same_tree(None, None) is True
    assert is_same_tree(TreeNode(1), None) is False
    print("all tests passed")