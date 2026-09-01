class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for num in sett:
            # Is this the start of a sequence?
            if num - 1 not in sett:
                current = num
                count = 1

                while current + 1 in sett:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest