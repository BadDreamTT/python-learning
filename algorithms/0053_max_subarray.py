"""LeetCode 53. 最大子数组和（中等）

思路：Kadane 算法。遍历时维护「以当前元素结尾的最大和」cur，
      每步 cur = max(当前元素, cur + 当前元素)，全局最大值随时更新。
时间复杂度：O(n)
空间复杂度：O(1)
"""


def max_sub_array(nums: list[int]) -> int:
    cur = best = nums[0]
    for num in nums[1:]:
        cur = max(num, cur + num)
        best = max(best, cur)
    return best


if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    print("all tests passed")
