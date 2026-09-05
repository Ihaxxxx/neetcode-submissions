class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        new = [0] * n
        for i in range(n):
            # looping until the last element which has a greater temperature
            while stack and temperatures[i] > stack[-1][0] :
                prev , index = stack.pop()
                new[index] = i - index   
            stack.append((temperatures[i],i))

        return new