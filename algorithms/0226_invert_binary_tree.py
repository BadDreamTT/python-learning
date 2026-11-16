"""LeetCode 226. 翻转二叉树（简单）

思路：BFS（队列）。每个节点出队时交换其左右孩子，
      再把交换后的两个孩子入队，直到队列为空。
      从尾巴排队，从脑袋办事。 append() 排队，popleft() 办事。
时间复杂度：O(n)
空间复杂度：O(w)，w 为树的最大宽度
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None

    queue = deque([root])
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return root


def same_tree(a: TreeNode | None, b: TreeNode | None) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.val == b.val
            and same_tree(a.left, b.left)
            and same_tree(a.right, b.right))


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    expected = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)),
                        TreeNode(2, TreeNode(3), TreeNode(1)))
    assert same_tree(invert_tree(root), expected) is True
    assert invert_tree(None) is None
    assert same_tree(invert_tree(TreeNode(1)), TreeNode(1)) is True
    print("all tests passed")