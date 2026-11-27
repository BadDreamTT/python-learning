"""LeetCode 33. 搜索旋转排序数组（中等）

思路：二分。旋转数组二分后，总有一半是有序的：
      若 nums[left] <= nums[mid]，左半有序，判断 target 是否在 [nums[left], nums[mid]) 内；
      否则右半有序，判断 target 是否在 (nums[mid], nums[right]] 内。
时间复杂度：O(log n)
空间复杂度：O(1)
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:              # 左半有序
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                                     # 右半有序
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    # ① 目标在右半段
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    # ② 目标在左半段
    assert search([4, 5, 6, 7, 0, 1, 2], 5) == 1

    # ③ 目标不存在
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # ④ 未旋转的普通有序数组
    assert search([1, 2, 3, 4, 5], 3) == 2

    # ⑤ 单元素：命中
    assert search([1], 1) == 0

    # ⑥ 单元素：未命中
    assert search([1], 0) == -1

    # ⑦ 两元素（测 left == mid 的情况）
    assert search([3, 1], 1) == 1
    assert search([3, 1], 3) == 0

    # ⑧ 旋转点在开头（等于未旋转）
    assert search([1, 2, 3, 4], 4) == 3

    print("all tests passed")