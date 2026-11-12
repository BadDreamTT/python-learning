"""LeetCode 20. 有效的括号（简单）

思路：一开始思路是,其实是一个个匹配,如果是右括号就弹栈看是否存在,如果匹配不上就返回False,但最后都是1组相互对应的,所以奇数直接就返回Fasle
如果循环到的数字不在pairs里面就是左括号,那么就存在st当中,如果不存在st当中或者弹栈不等于当前值报False
时间复杂度：O(n)
空间复杂度：O(n)
"""


def is_valid(s: str) -> bool:
   st = []
        if len(s) % 2:
            return False
        
        pairs = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c not in pairs:
                st.append(c)
            elif not st or st.pop() != pairs[c]:
                return False
        return not st


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("(((") is False
    assert is_valid(")") is False
    assert is_valid("") is True
    print("all tests passed")
