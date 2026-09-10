class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        answer = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            answer = max(answer, right - left + 1)

        return answer