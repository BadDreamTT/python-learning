"""LeetCode 21. 合并两个有序链表（简单）

思路：递归。两个表相互比较值,。
时间复杂度：O(m + n)
空间复杂度：O(m + n)（递归调用栈，最坏是两链表长度之和）
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list2.next, list1)
        return list2


def to_list(head: ListNode | None) -> list[int]:
    """辅助：链表 -> 列表，方便 assert"""
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def build(vals: list[int]) -> ListNode | None:
    """辅助：列表 -> 链表"""
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    assert to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(merge_two_lists(build([]), build([]))) == []
    assert to_list(merge_two_lists(build([]), build([0]))) == [0]
    print("all tests passed")