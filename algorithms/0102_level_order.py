from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(t) == [[3], [9, 20], [15, 7]]
    assert level_order(None) == []
    assert level_order(TreeNode(1)) == [[1]]
    print("all tests passed")