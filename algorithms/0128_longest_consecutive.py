"""LeetCode 128. 最长连续序列（中等）

思路:一开始想到暴力循环,但循环的话重复太多,所以加了判断如果当前数-1也存在字典中,那当前数就不是起始点
就从下一个开始,知道遇到起始点,开始＋。
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
