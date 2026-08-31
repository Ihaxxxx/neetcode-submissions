class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ''
        for val in strs:
            new += f'{len(val)}#{val}'
        return new

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            content = s[j+1:j+1+length]
            i = j + 1 + length
            strs.append(content)
        return strs