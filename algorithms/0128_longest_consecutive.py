"""LeetCode 128. 最长连续序列（中等）

思路：把所有数字放进 set；只从「序列起点」（x-1 不在 set 里）开始向后数，
      避免重复遍历，整体仍是 O(n)。
时间复杂度：O(n)
空间复杂度：O(n)
"""


def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    best = 0
    for x in num_set:
        if x - 1 not in num_set:      # 只从序列的起点开始数
            cur = x
            length = 1
            while cur + 1 in num_set:
                cur += 1
                length += 1
            best = max(best, length)
    return best


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([1, 0, 1, 2]) == 3
    assert longest_consecutive([]) == 0
    print("all tests passed")
