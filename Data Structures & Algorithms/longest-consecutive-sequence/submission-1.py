class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        max_length = 0

        for num in nums:
            nums_set.add(num)

        for element in nums_set:
            if element - 1 not in nums_set:
                length = 0
                while element + length in nums_set:
                    length += 1

                if max_length < length:
                    max_length = length

    
        return max_length