"""LeetCode 1. 两数之和（简单）

思路：用字典记录「元素值 -> 下标」，遍历时检查 target - 当前值 是否已在字典里。
时间复杂度：O(n)
空间复杂度：O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("all tests passed")
