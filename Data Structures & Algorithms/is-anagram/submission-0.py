class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {} 
        for item in s:
            if item not in maps:
                maps[item] = 1
            else:
                maps[item] += 1
        
        for item in t:
            if item not in mapt:
                mapt[item] = 1
            else:
                mapt[item] += 1
        
        return maps == mapt