"""LeetCode 283. 移动零（简单）

思路：双指针。slow 指向「下一个非零元素该放的位置」，
      fast 遍历数组，遇到非零就与 slow 交换，然后 slow 后移。
时间复杂度：O(n)
空间复杂度：O(1)（原地修改）
"""


def move_zeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    assert a == [1, 3, 12, 0, 0], a

    b = [0]
    move_zeroes(b)
    assert b == [0], b
    print("all tests passed")
