import string

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = {}

        for str in strs:
            current_str_dict = {c: 0 for c in string.ascii_lowercase}
            for char in str:
                current_str_dict[char] += 1

            key = tuple(current_str_dict.values())

            if key in anagrams_groups:
                anagrams_groups[key].append(str)
            else:
                anagrams_groups[key] = [str]

        result = list(anagrams_groups.values())
        return result