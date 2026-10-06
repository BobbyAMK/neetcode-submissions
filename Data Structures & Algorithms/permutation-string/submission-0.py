class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = Counter(s1)
        dict_s2 = Counter(s2[:len(s1)])

        if dict_s1 == dict_s2:
            return True
        for i in range(len(s1), len(s2)):
            right_char = s2[i]
            dict_s2[right_char] = dict_s2.get(right_char, 0) + 1

            left_char = s2[i - len(s1)]
            dict_s2[left_char] -= 1

            if dict_s2[left_char] == 0:
                del dict_s2[left_char]
            
            if dict_s1 == dict_s2:
                return True
        return False