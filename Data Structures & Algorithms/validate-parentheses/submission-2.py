class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in '[({':
                stack.append(item)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if val == '[' and item == ']':
                    continue
                elif val == '(' and item == ')':
                    continue
                elif val == '{' and item == '}':
                    continue
                else:
                    return False
        return len(stack) == 0