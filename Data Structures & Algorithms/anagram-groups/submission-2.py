import string

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = {}
        
        for str_index, str in enumerate(strs):
            current_str_dict = {c: 0 for c in string.ascii_lowercase}
            for char in str:
                current_str_dict[char] += 1

            key = tuple(current_str_dict.values())

            if key in anagrams_groups:
                anagrams_groups[key].append(str_index)
            else:
                anagrams_groups[key] = [str_index]

        result = [[strs[i] for i in group] for group in anagrams_groups.values()]
        return result