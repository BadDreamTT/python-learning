"""LeetCode 34. 在排序数组中查找元素的第一个和最后一个位置（中等）

思路：两次二分。
      get_left  ：找"第一个 ≥ target"的位置（下界）
      get_right ：找"最后一个 ≤ target"的位置（上界）
      若 left 越界或 nums[left] != target，说明 target 不存在。
时间复杂度：O(log n)
空间复杂度：O(1)
"""


def search_range(nums: list[int], target: int) -> list[int]:
    def get_left() -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:      # 大于等于：把右边界往左压
                right = mid - 1
            else:
                left = mid + 1
        return left                      # 第一个 ≥ target 的位置

    def get_right() -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:      # 小于等于：把左边界往右推
                left = mid + 1
            else:
                right = mid - 1
        return right                     # 最后一个 ≤ target 的位置

    left = get_left()

    # 越界 或 该位置不是 target → 不存在
    if left >= len(nums) or nums[left] != target:
        return [-1, -1]

    return [left, get_right()]


if __name__ == "__main__":
    # ① 正常：目标出现两次
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]

    # ② 目标只出现一次
    assert search_range([5, 7, 7, 8, 8, 10], 5) == [0, 0]

    # ③ 目标不存在（在中间）
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

    # ④ 目标比所有元素都小（测越界保护）
    assert search_range([5, 7, 7, 8, 8, 10], 1) == [-1, -1]

    # ⑤ 目标比所有元素都大（left 会等于 len(nums)）
    assert search_range([5, 7, 7, 8, 8, 10], 11) == [-1, -1]

    # ⑥ 空数组
    assert search_range([], 0) == [-1, -1]

    # ⑦ 单元素：命中
    assert search_range([1], 1) == [0, 0]

    # ⑧ 单元素：未命中
    assert search_range([1], 2) == [-1, -1]

    # ⑨ 全部元素相同
    assert search_range([2, 2, 2, 2], 2) == [0, 3]

    # ⑩ 大数组：验证复杂度
    big = [0] * 500_000 + [1] * 500_000
    assert search_range(big, 1) == [500_000, 999_999]

    print("all tests passed")