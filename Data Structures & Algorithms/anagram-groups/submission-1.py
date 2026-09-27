class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_count_arr = []

        for str in strs:
            letter_count_array = [0] * 26

            for char in str:
                letter_count_array[ord(char) - 97] += 1

            strs_count_arr.append(tuple(letter_count_array))

        grouped = {}
        for i in range(len(strs)):
            if strs_count_arr[i] in grouped:
                grouped[strs_count_arr[i]].append(strs[i])
            else:
                grouped[strs_count_arr[i]] = [strs[i]]

        return list(grouped.values())
        


        