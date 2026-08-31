class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}
        while strs:
            original = strs.pop(0)
            sorted_original = tuple(sorted(original))
            if sorted_original in mapp:
                mapp[sorted_original].append(original)
            else:
                mapp[sorted_original] = [original]

        return list(mapp.values())