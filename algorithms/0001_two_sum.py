"""LeetCode 1. 两数之和（简单）

思路:开始想的是暴力双循环,后面优化时间,想到哈希表,将所有数值存在字典[数值:下标],用target-num得到需要的一个数.
在判断这个数是否在字典里面,存在直接返回两个下标.不存在就把这个数存进表里,后续使用
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
