"""LeetCode 35. 搜索插入位置（简单）

思路：二分查找。与 704 唯一区别是"找不到时返回 left"——
      循环结束时 left 指向第一个 ≥ target 的位置，正好是插入点。
时间复杂度：O(log n)
空间复杂度：O(1)
"""


def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left          # 指针越界，left 就是应插入的位置


if __name__ == "__main__":
    # ① 目标存在：返回下标
    assert search_insert([1, 3, 5, 6], 5) == 2

    # ② 目标不存在：插在中间
    assert search_insert([1, 3, 5, 6], 2) == 1

    # ③ 目标不存在：插在末尾（= len(nums)）
    assert search_insert([1, 3, 5, 6], 7) == 4

    # ④ 目标不存在：插在开头（= 0）
    assert search_insert([1, 3, 5, 6], 0) == 0

    # ⑤ 单元素：命中
    assert search_insert([1], 1) == 0

    # ⑥ 单元素：比它小 → 插在 0
    assert search_insert([1], 0) == 0

    # ⑦ 单元素：比它大 → 插在 1
    assert search_insert([1], 2) == 1

    # ⑧ 全部命中首尾
    assert search_insert([1, 3], 1) == 0
    assert search_insert([1, 3], 3) == 1

    # ⑨ 大数组：验证是 O(log n)
    big = list(range(0, 1_000_000, 2))
    assert search_insert(big, 500_001) == 250_001

    print("all tests passed")