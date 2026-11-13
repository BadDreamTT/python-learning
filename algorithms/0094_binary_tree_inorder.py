"""LeetCode 94. 二叉树的中序遍历（简单）

思路：递归。中序 = 左子树 → 根 → 右子树。
时间复杂度：O(n)，每个节点访问一次
空间复杂度：O(h)，h 为树高（递归栈深度），最坏 O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode | None) -> list[int]:
    res = []

    def walk(node):
        if node is None:
            return
        walk(node.left)
        res.append(node.val)
        walk(node.right)

    walk(root)
    return res


if __name__ == "__main__":
    # 示例 1: 1 -> 右 2 -> 左 3
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorder_traversal(root) == [1, 3, 2]

    #      1
    #     / \
    #    2   3
    assert inorder_traversal(TreeNode(1, TreeNode(2), TreeNode(3))) == [2, 1, 3]
    assert inorder_traversal(None) == []
    print("all tests passed")