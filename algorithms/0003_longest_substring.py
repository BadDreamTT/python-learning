"""LeetCode 3. 无重复字符的最长子串（中等）

思路：滑动窗口。right 每步右移，把字符放进窗口 set；
      若重复则 left 不断右移并移出字符，直到窗口无重复；
      每步更新 max_length = max(best, right - left + 1)。
时间复杂度：O(n)  —— left 和 right 都不回头，每个字符最多进出各一次
空间复杂度：O(k)  —— k 为字符集大小
"""


def length_of_longest_substring(s: str) -> int:
   seen=set()
        left=0
        max_length=0
        for right,char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(char)
            max_length=max(max_length,right-left+1)
        return max_length


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    print("all tests passed")
