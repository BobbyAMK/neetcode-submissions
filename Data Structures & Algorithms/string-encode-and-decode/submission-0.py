class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '_' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '_':
                j += 1
            word_len = int(s[i:j])
            result.append(s[j+1 : j+1 + word_len])
            i = j + 1 + word_len
        return result
