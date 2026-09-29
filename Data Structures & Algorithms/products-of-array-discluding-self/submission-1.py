class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_of_zeros = 0
        product_of_all = 1

        for num in nums:
            if num != 0:
                product_of_all = product_of_all * num
            else:
                num_of_zeros += 1

        result = []

        if num_of_zeros > 1:
            return [0] * len(nums)

        for num in nums:
            if num == 0:
                result.append(product_of_all)
            else:
                if num_of_zeros == 0:
                    result.append(int(product_of_all / num))
                else:
                    result.append(0)

        return result