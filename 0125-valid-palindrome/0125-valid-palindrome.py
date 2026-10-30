class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        for letter in s:
            if letter.isalnum():
                cleaned += letter.lower()

        return cleaned == cleaned[::-1]