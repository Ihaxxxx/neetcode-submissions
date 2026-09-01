class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        return s_low == s_low[::-1]