class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}_{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            j = s.find('_', i)
            word_len = int(s[i:j])
            result.append(s[j+1 : j+1 + word_len])
            i = j + 1 + word_len
        return result
