class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r:
            if target > nums[r] or target < nums[l]:
                return -1
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                return m