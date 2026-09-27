class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dictionary = make_dictionary(s)
        t_dictionary = make_dictionary(t)
        for key in s_dictionary:
            if key not in t_dictionary:
                return False
            elif s_dictionary[key] != t_dictionary[key]:
                return False
        return True
        
def make_dictionary(string):
    dic = {}
    for char in string:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 0

    return dic