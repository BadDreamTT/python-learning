class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(nums, target):
            left,right = 0,len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        return binary_search(nums,target)


if __name__ == "__main__":
    s = Solution()

    # ① 正常找到：目标在中间
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4

    # ② 目标不存在：应返回 -1
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # ③ 目标在第一个位置（左边界）
    assert s.search([1, 3, 5], 1) == 0

    # ④ 目标在最后一个位置（右边界）
    assert s.search([1, 3, 5], 5) == 2

    # ⑤ 只有一个元素：命中
    assert s.search([7], 7) == 0

    # ⑥ 只有一个元素：未命中
    assert s.search([7], 3) == -1

    # ⑦ 比所有元素都小
    assert s.search([2, 4, 6], 1) == -1

    # ⑧ 比所有元素都大
    assert s.search([2, 4, 6], 99) == -1

    # ⑨ 空列表（LeetCode 不测，但验证边界写法是否安全）
    assert s.search([], 5) == -1

    # ⑩ 大数组：证明是 O(log n) 而不是 O(n)
    big = list(range(0, 1_000_000, 2))        # 50 万个元素
    assert s.search(big, 888_888) == 444_444

    print("all tests passed")
