"""LeetCode 206. 反转链表（简单）

思路：三指针。遍历时把 cur.next 指向 prev，用 tmp 记住原来的 next；
      走完一遍 prev 就是新头节点。
时间复杂度：O(n)
空间复杂度：O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    cur = head
    while cur is not None:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev


def to_list(head: ListNode | None) -> list[int]:
    """辅助函数：把链表转成列表，方便 assert"""
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert to_list(reverse_list(head)) == [5, 4, 3, 2, 1]
    assert reverse_list(None) is None
    assert to_list(reverse_list(ListNode(1))) == [1]
    print("all tests passed")