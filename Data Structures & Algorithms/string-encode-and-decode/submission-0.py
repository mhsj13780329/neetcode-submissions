class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = ""
        lengths = [len(str) for str in strs]

        for i in range(len(strs)):
            encoded_strings += str(lengths[i])
            encoded_strings += "#"
            encoded_strings += strs[i]

        return encoded_strings
    def decode(self, encoded_string: str) -> List[str]:
        decoded_strings = []

        i = 0
        while i < len(encoded_string):

            cur_str_len = ""

            while encoded_string[i] != "#":
                cur_str_len += encoded_string[i]
                i += 1

            cur_str_len = int(cur_str_len)
            i += 1
            decoded_strings.append(encoded_string[i : i + cur_str_len])
            i += cur_str_len

        return decoded_strings