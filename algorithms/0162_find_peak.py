"""LeetCode 162. 寻找峰值（中等）

思路：二分。比较 nums[mid] 与 nums[mid+1]：
      上升（nums[mid] < nums[mid+1]）→ 峰值在右侧，left = mid + 1
      下降（nums[mid] > nums[mid+1]）→ 峰值在左侧或就是 mid，right = mid
      补充一点,这个返回left.其实当你再看到这个迷糊的时候你就自己把循环自己跑一边就知道了.
时间复杂度：O(log n)
空间复杂度：O(1)
"""


def find_peak_element(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:                      # 注意是 <，不是 <=
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:        # 下坡 → 峰值在左（含 mid）
            right = mid
        else:                                # 上坡 → 峰值在右
            left = mid + 1

    return left                              # left == right，即峰值下标


if __name__ == "__main__":
    # ① 峰值在中间
    assert find_peak_element([1, 2, 3, 1]) == 2

    # ② 多个峰值，返回任一即可
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) in (1, 5)

    # ③ 单调递增 → 峰值是最后一个
    assert find_peak_element([1, 2, 3, 4]) == 3

    # ④ 单调递减 → 峰值是第一个
    assert find_peak_element([4, 3, 2, 1]) == 0

    # ⑤ 单元素
    assert find_peak_element([1]) == 0

    # ⑥ 两元素
    assert find_peak_element([1, 2]) == 1
    assert find_peak_element([2, 1]) == 0

    print("all tests passed")