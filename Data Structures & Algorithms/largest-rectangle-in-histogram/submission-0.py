class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                height = heights[idx]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        # Process bars that never found a smaller bar on the right
        n = len(heights)

        while stack:
            idx = stack.pop()
            height = heights[idx]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            max_area = max(max_area, height * width)

        return max_area