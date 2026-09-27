class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_freq_dict = {}
        for num in nums:
            if num in element_freq_dict:
                element_freq_dict[num] += 1
            else:
                element_freq_dict[num] = 0

        sorted_by_freq = sorted(element_freq_dict, key=element_freq_dict.get, reverse=True)
        return sorted_by_freq[:k]