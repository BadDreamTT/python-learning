"""LeetCode 49. 字母异位词分组（中等）

思路：用sorted把每个字符拆出来然后排序,如果字典里有这个key就返回对应的值,没有就插入,然后返回空列表。
时间复杂度：O(n * k log k)，k 为字符串最大长度
空间复杂度：O(n * k)
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for s in strs:
        key = "".join(sorted(s))
        groups.setdefault(key, []).append(s)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # 分组顺序不固定，所以比较时先规整化
    actual = sorted(sorted(g) for g in result)
    expected = sorted(sorted(g) for g in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert actual == expected, actual
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("all tests passed")
