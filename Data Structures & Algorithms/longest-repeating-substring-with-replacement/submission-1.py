class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {}
        res = 0

        slow = 0
        maxf = 0

        for fast in range(len(s)):
            table[s[fast]] = 1 + table.get(s[fast],0)

            maxf = max(maxf,table[s[fast]])

            while (fast-slow+1) - maxf > k:
                table[s[slow]] -= 1
                slow += 1
            res = max(res, fast - slow + 1)

        return res
