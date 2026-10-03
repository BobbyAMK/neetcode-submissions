class Solution:
    def isPalindrome(self, s: str) -> bool:
        formated_text = re.sub(r"\W+", "", s).lower()
        print(formated_text)
        left, right = 0, len(formated_text) - 1
        while left < right:
            if formated_text[left] == formated_text[right]:
                left += 1
                right -= 1
            else:
                return False
        return True