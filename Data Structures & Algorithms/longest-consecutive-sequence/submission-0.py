class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        seq_lengths = []

        for num in nums:
            nums_set.add(num)

        for element in nums_set:
            if element - 1 not in nums_set:
                length = 0
                while element + length in nums_set:
                    length += 1

                seq_lengths.append(length)

        max = 0
        for length in seq_lengths:
            if length > max:
                max = length

        return max