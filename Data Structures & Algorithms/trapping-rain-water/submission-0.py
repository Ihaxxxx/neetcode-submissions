class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = [height[0]] * len(height)
        suffixMax = [height[-1]] * len(height)

        for i in range(1,len(height)):
            prefixMax[i] = max(prefixMax[i-1],height[i])

        for j in range(len(height)-2,-1,-1):
            suffixMax[j] = max(suffixMax[j+1],height[j])
        
        summ = 0

        for k in range(len(height)):
            summ += min(prefixMax[k],suffixMax[k]) - height[k]
        
        return summ
