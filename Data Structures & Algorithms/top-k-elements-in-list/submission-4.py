class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_freq_dict = {}
        for num in nums:
            if num in elements_freq_dict:
                elements_freq_dict[num] += 1
            else:
                elements_freq_dict[num] = 1

        buckets = {}
        for i in range(1, len(nums) + 2):
            buckets[i] = []

        for key in elements_freq_dict:
            buckets[elements_freq_dict[key]].append(key)

        result = []
        for key in reversed(buckets):
            if len(result) < k:
                for number in buckets[key]:
                    result.append(number)

        return result