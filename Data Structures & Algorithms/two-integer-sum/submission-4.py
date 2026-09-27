class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}

        for i in range(len(nums)):
            nums_dic[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dic:
                if i != nums_dic[complement]:
                    return [i, nums_dic[complement]]