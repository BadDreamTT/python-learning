"""LeetCode 141. 环形链表（简单）

思路：快慢指针。slow 每次走 1 步，fast 每次走 2 步；
      有环时 fast 一定会在环里"追上"slow，无环时 fast 会先走到 None。
时间复杂度：O(n)
空间复杂度：O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:          # 注意：比较的是"是不是同一个节点"，不是 val
            return True

    return False


def build_with_cycle(vals: list[int], pos: int) -> ListNode | None:
    """辅助：按列表建链，并把尾节点接回下标 pos 的节点（-1 表示无环）"""
    dummy = ListNode(0)
    cur = dummy
    nodes = []
    for v in vals:
        node = ListNode(v)
        cur.next = node
        cur = node
        nodes.append(node)
    if pos >= 0 and nodes:
        cur.next = nodes[pos]
    return dummy.next


if __name__ == "__main__":
    assert has_cycle(build_with_cycle([3, 2, 0, -4], 1)) is True
    assert has_cycle(build_with_cycle([1, 2], 0)) is True
    assert has_cycle(build_with_cycle([1], -1)) is False
    assert has_cycle(build_with_cycle([], -1)) is False
    print("all tests passed")