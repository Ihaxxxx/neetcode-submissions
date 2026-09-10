class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        left = 0
        window = set()   
        answer = 1
        for right in range(len(s)):
            if s[right] not in window:
                window.add(s[right])
            else:
                while s[right] in window:
                    window.discard(s[left])
                    left += 1                    
                window.add(s[right])

            answer = max(answer,right - left + 1)
        
        return answer