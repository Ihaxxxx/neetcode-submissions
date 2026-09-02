class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in "+-/*":
                stack.append(int(item))
            else:
                b = stack.pop()
                a = stack.pop()

                if item == "+":
                    ans = a + b
                elif item == "-":
                    ans = a - b
                elif item == "*":
                    ans = a * b
                elif item == "/":
                    ans = int(a / b)

                stack.append(ans)

        return stack[-1]